from flask import Blueprint, render_template, request, flash, redirect, url_for, send_from_directory, make_response, \
    Response
from werkzeug.utils import secure_filename
import tensorflow as tf
import random
import cv2
import os
import time

from models import products, cropped
from middlewares.yolo import detect
from middlewares.knn import get_neighbors

import re
import base64
import numpy as np

upload_api = Blueprint('upload_api', __name__)

UPLOAD_FOLDER = 'upload'
ALLOWED_EXTENSIONS = {'jpg', 'jpeg'}


# def load_and_preprocess_image(path):
#     '''
#     Read file from path
#     :param path:
#     :return:
#     '''
#     image = tf.io.read_file(path)
#     return preprocess_image(image)

# def generate_img():
#     cap = cv2.VideoCapture(0)

#     cap.set(3, 640)
#     cap.set(4, 480)

#     i = 1

#     while(True):
#         # if button_is_pressed:

#             # Capture frame-by-frame
#         ret, frame = cap.read()
#         i+=1
#         #     img = preprocess_image(frame)
#         #     img = yolov3(img)
#         #     img = img + bounding_boxes
#         #     push new image to canvas of frontend

#         # if i % 20 == 0:
#             # predict = do(frame)
#             # cv2.putText(frame)


#             # return bounding box
#         #     draw on frame 
#         #     have_boundingbox_frame = frame

#         # Display the resulting frame


#         if ret:
#             # flag, jpeg = cv2.imencode('.jpg', have_boundingbox_frame)

#             flag, jpeg = cv2.imencode('.jpg', frame)
#             b = jpeg.tobytes()

#         else:
#             continue
        
#         if flag:

#             yield (b'--frame\r\n'
#                 b'Content-Type: image/jpeg\r\n\r\n' + b + b'\r\n\r\n')

#         else:
#             continue

#         # When everything done, release the capture
#         # cap.release() 
#         # cv2.destroyAllWindows()
    
# @upload_api.route('/video_feed')
# def video_feed():
#     return Response(generate_img(),
#                     mimetype='multipart/x-mixed-replace; boundary=frame')


import uuid

def parse_image(imgData):
    img_str = re.search(b"base64,(.*)", imgData).group(1)
    img_decode = base64.decodebytes(img_str)
    filename = "{}.jpg".format(uuid.uuid4().hex)
    with open('static/images/'+filename, "wb") as f:
        f.write(img_decode)
    return 'static/images/'+filename

# def preprocess(image):
#     image = tf.image.decode_jpeg(image, channels=3)
#     image = tf.image.resize(image, [299, 299])
#     image = image.numpy().reshape((1,299,299,3))
#     image = image/255.0
#     return image

@upload_api.route('/webcam_upload', methods =["POST"])
def webcam_upload():
    data = request.get_json()

    # Preprocess the upload image
    img_raw = data['data-uri'].encode()
    image_path = parse_image(img_raw)
    print(image_path)
    (categoryPredict, positions) = detect(image_path)
    print(categoryPredict)

    if len(categoryPredict) > 0:
        croppedDectection = []
        for i in range(len(categoryPredict)):
            croppedDectection.append('static/images/cropped-dectecion-{}.jpg'.format(i))

        croppedObject = cropped.list_object(zip(categoryPredict, croppedDectection))
    else: 
        croppedDectection = None

    objectDetection = 'static/images/object-detection.jpg'

    os.remove(image_path)

    return {"crop":croppedDectection,"full":objectDetection, "details": positions}
    

    # return {"status":"success"}