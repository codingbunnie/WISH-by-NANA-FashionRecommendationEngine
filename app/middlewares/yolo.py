import time
import cv2
import argparse
import numpy as np
import math
import requests
from PIL import Image

categoryID = {
    0 : 'top',
    1 : 'shorts',
    2 : 'skirt',
    3 : 'dress',
    4 : 'trousers'
    
}

classes = None

namePath = 'static/yolo/obj.names'
weightsPath = 'static/yolo/yolov3.weights'
configPath = 'static/yolo/yolov3.cfg'

addr = 'http://localhost:5000'
url = addr + '/video'

content_type = 'image/jpeg'
headers = {'content-type': content_type}

net = cv2.dnn.readNet(weightsPath,configPath) # Original yolov3
classes = []
with open(namePath,"r") as f:
    classes = [line.strip() for line in f.readlines()]
colors = np.random.uniform(0,255,size=(len(classes),3))
font = cv2.FONT_HERSHEY_PLAIN

def get_output_layers(net):
    
    layer_names = net.getLayerNames()
    output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]

    return output_layers


def draw_prediction(img, class_id, confidence, x, y, x_plus_w, y_plus_h, colors):
    
    label = str(classes[class_id])
    color = colors[class_id]
    cv2.rectangle(img, (x , y), (x_plus_w, y_plus_h), color, round(0.01*x))
    
    # if label != 'top':
    #     cv2.putText(img, label, (x , y), cv2.FONT_HERSHEY_SIMPLEX, 2, color, round(0.01*x))
    
    # else: #top
    #     cv2.putText(img, label, (x , y - 20), cv2.FONT_HERSHEY_SIMPLEX, 2, color, round(0.01*x))
    cv2.putText(img, label, (x , y), font, math.ceil(0.01*x), color, math.ceil(0.01*x))
        
def detect(imagePath):

    global classes
    
    image = cv2.imread(imagePath)

    Width = image.shape[1]
    Height = image.shape[0]
    scale = 0.00392

    with open(namePath, 'r') as f:
        classes = [line.strip() for line in f.readlines()]

    COLORS = np.random.uniform(0, 255, size=(len(classes), 3))

    net = cv2.dnn.readNet(weightsPath, configPath)
    blob = cv2.dnn.blobFromImage(image, scale, (416, 416), (0, 0, 0), True, crop = False)
    net.setInput(blob)

    outs = net.forward(get_output_layers(net))

    class_ids = []
    confidences = []
    boxes = []
    conf_threshold = 0.4
    nms_threshold = 0.6

    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            
            if confidence > 0.1:
                
                center_x = int(detection[0] * Width)
                center_y = int(detection[1] * Height)
                w = int(detection[2] * Width)
                h = int(detection[3] * Height)
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)
                

                class_ids.append(class_id)
                confidences.append(float(confidence))
                boxes.append([x, y, w, h])

    indices = cv2.dnn.NMSBoxes(boxes, confidences, conf_threshold, nms_threshold)

    categoryPredict = []
    imagePrediction = image.copy()

    if len(indices) > 0:
        for j,i in enumerate(indices):
            i = i[0]
            x,y,w,h = boxes[i]
            label = str(classes[class_ids[i]]) 
            color = colors[class_ids[i]]
            cv2.rectangle(imagePrediction,(x,y),(x+w,y+h),color,2)
            cv2.putText(imagePrediction,label.capitalize(),(x,y-10),font,2,color,2)


    # positions = []


    #         i = i[0]
            
    #         box = boxes[i]
    #         x = box[0]
    #         y = box[1]
    #         w = box[2]
    #         h = box[3]
            
    #         draw_prediction(imagePrediction, class_ids[i], confidences[i], round(x), round(y), round(x + w), round(y + h), COLORS)

            categoryPredict.append(classes[class_ids[i]])  

            croppedImage = image[y:y+h,x:x+w]

            # positions.append([x, y, w, h, classes[class_id]])  

            cv2.imwrite("static/images/cropped-dectecion-{}.jpg".format(j), croppedImage)    

    cv2.imwrite("static/images/object-detection.jpg", imagePrediction)

    # _, img_encoded = cv2.imencode('.jpg', imagePrediction)

    # response = requests.post(test_url, data=img_encoded.tostring(), headers=headers)

    # print(json.loads(response.text))

    return categoryPredict# , positions

class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        self.video.release()

    def get_frame(self, capture = False):



        starting_time = time.time()

        outputlayers = get_output_layers(net)
        frame_id = 0

        _, frame = self.video.read()

        if capture:
            cv2.imwrite("static/images/object-detection.jpg", frame)

        frame_id +=1

        height, width, _ = frame.shape

        blob = cv2.dnn.blobFromImage(frame,0.00392,(320,320),(0,0,0),True,crop=False)

        net.setInput(blob)
        outs = net.forward(outputlayers)

        class_ids=[]
        confidences=[]
        boxes=[]
        for out in outs:
            for detection in out:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                if confidence > 0.3:
                    #onject detected
                    center_x= int(detection[0]*width)
                    center_y= int(detection[1]*height)
                    w = int(detection[2]*width)
                    h = int(detection[3]*height)

                    x=int(center_x - w/2)
                    y=int(center_y - h/2)

                    boxes.append([x,y,w,h]) #put all rectangle areas
                    confidences.append(float(confidence)) #how confidence was that object detected and show that percentage
                    class_ids.append(class_id) #name of the object tha was detected

        indexes = cv2.dnn.NMSBoxes(boxes,confidences,0.4,0.6)

        for i in range(len(boxes)):
            if i in indexes:
                x,y,w,h = boxes[i]
                label = str(classes[class_ids[i]])
                confidence= confidences[i]
                color = colors[class_ids[i]]
                cv2.rectangle(frame,(x,y),(x+w,y+h),color,2)
                cv2.putText(frame,label+" "+str(round(confidence,2)),(x,y+30),font,1,(255,255,255),2)

        elapsed_time = time.time() - starting_time
        fps = frame_id/elapsed_time
        cv2.putText(frame,"FPS:"+str(round(fps,2)),(10,50),font,2,(0,0,0),1)
        
        _, jpeg = cv2.imencode('.jpg', frame)


        return jpeg.tobytes()














# def detect_tom(imagePath):

#     global classes
#     positions = []
    
#     image = cv2.imread(imagePath)

#     Width = image.shape[1]
#     Height = image.shape[0]
#     scale = 0.00392

#     with open(namePath, 'r') as f:
#         classes = [line.strip() for line in f.readlines()]

#     COLORS = np.random.uniform(0, 255, size=(len(classes), 3))

#     net = cv2.dnn.readNet(weightsPath, configPath)
#     blob = cv2.dnn.blobFromImage(image, scale, (416, 416), (0, 0, 0), True, crop = False)
#     net.setInput(blob)

#     outs = net.forward(get_output_layers(net))

#     class_ids = []
#     confidences = []
#     boxes = []
#     conf_threshold = 0.5
#     nms_threshold = 0.4

#     for out in outs:
#         for detection in out:
#             scores = detection[5:]
#             class_id = np.argmax(scores)
#             confidence = scores[class_id]
            
#             if confidence > 0.1:
                
#                 center_x = int(detection[0] * Width)
#                 center_y = int(detection[1] * Height)
#                 w = int(detection[2] * Width)
#                 h = int(detection[3] * Height)
#                 x = center_x - w / 2
#                 y = center_y - h / 2

#                 positions.append([x, y, w, h, classes[class_id]])              

#                 class_ids.append(class_id)
#                 confidences.append(float(confidence))
#                 boxes.append([x, y, w, h])

#     indices = cv2.dnn.NMSBoxes(boxes, confidences, conf_threshold, nms_threshold)

#     categoryPredict = []
#     imagePrediction = image.copy()


#     import os, glob
#     for filename in glob.glob("static/images/cropped-dectecion*"):
#         os.remove(filename) 
#     for filename in glob.glob("static/images/object-detection*"):
#         os.remove(filename) 

#     if len(indices) > 0:
#         for j,i in enumerate(indices):

#             i = i[0]
            
#             box = boxes[i]
#             x = box[0]
#             y = box[1]
#             w = box[2]
#             h = box[3]
            
#             if classes[class_ids[i]] == 'top':
                
#                 draw_prediction(imagePrediction, class_ids[i], confidences[i], round(x) - 50, round(y) - 50, round(x + w) + 50, round(y + h), COLORS)
                
#             elif classes[class_ids[i]] in ['dress', 'trousers']:
            
#                 draw_prediction(imagePrediction, class_ids[i], confidences[i], round(x), round(y) - 80, round(x + w), round(y + h) + 80, COLORS)
                
#             else: 
#                 draw_prediction(imagePrediction, class_ids[i], confidences[i], round(x), round(y), round(x + w), round(y + h), COLORS)

#             categoryPredict.append(classes[class_ids[i]])  

#             croppedImage = image[round(y):round(y + h),round(x):round(x + w)]

#             cv2.imwrite("static/images/cropped-dectecion-{}.jpg".format(j), croppedImage)    

#     cv2.imwrite("static/images/object-detection.jpg", imagePrediction)

#     return (categoryPredict, positions)

