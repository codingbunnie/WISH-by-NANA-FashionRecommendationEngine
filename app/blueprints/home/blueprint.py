from flask import Blueprint, render_template, request, Response
import cv2, time, os, base64
from models import products, cropped
from middlewares.yolo import detect, VideoCamera
from middlewares.knn import get_neighbors
import pandas as pd
import pickle

home = Blueprint('home', __name__)
path = os.path.dirname(os.path.abspath(__file__))
ptuf = os.path.join(path, "../../static/images")


@home.route('/video', methods=["GET","POST"])
def video():
    if request.method == "POST":
        print(request)
        _ = VideoCamera().get_frame(capture = True)

        categoryPredict = detect('static/images/object-detection.jpg')

        if len(categoryPredict) > 0:
            croppedDectection = []
            for i in range(len(categoryPredict)):
                croppedDectection.append('images/cropped-dectecion-{}.jpg'.format(i))

            croppedObject = cropped.list_object(zip(categoryPredict, croppedDectection))
        else: 
            croppedObject = None

        return render_template('home.html',f='static/images/object-detection.jpg', c=croppedObject)
    
    return render_template('home.html', f = None, c = [])

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@home.route('/video_feed')
def videoFeed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@home.route("/still", methods=["GET","POST"])
def still():
    if request.method == "POST":
        f = request.files["uploadfile"]
        
        _, ext = os.path.splitext(f.filename)
        if os.path.exists(os.path.join(ptuf,"input"+ ext)):
            os.remove(os.path.join(ptuf,"input" + ext))

        f.save(os.path.join(ptuf,"input"+ ext))

        categoryPredict = detect('static/images/input.jpg')
        if len(categoryPredict) > 0:
            croppedDectection = []
            for i in range(len(categoryPredict)):
                croppedDectection.append('images/cropped-dectecion-{}.jpg'.format(i))

            croppedObject = cropped.list_object(zip(categoryPredict, croppedDectection))
        else: 
            croppedObject = None

        objectDetection = 'images/object-detection.jpg'

        return render_template('still.html', f=objectDetection, c=croppedObject)
        
    df = pd.read_csv('static/product-data/top.csv')

    for category in ['dress','shorts','skirt','trousers']:
        df.append(pd.read_csv('static/product-data/{}.csv'.format(category)))

    randomProducts = products.random_products(df, 10)

    return render_template('still.html', r=randomProducts)




@home.route("/recommend", methods=["POST"])
def recommend():

    category = request.args.get('category')
    path = request.args.get('path')

    knn = get_neighbors(category, path)

    df = pd.read_csv('static/product-data/{}.csv'.format(category))

    df = df.iloc[knn[1][0]]

    data = products.list_products(df)

    return render_template("recommend.html", f=path, products = data[:20])

@home.route("/")
def home_page():
    return render_template('index.html')


