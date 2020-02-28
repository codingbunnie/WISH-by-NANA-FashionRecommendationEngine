from flask import Flask, render_template, redirect, url_for
from blueprints import *
import cv2
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = "feij134#$qaf3%QERFAF"  # Flask secret key
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0
app.register_blueprint(home)  # blueprint for Home
app.register_blueprint(upload_api)  # blueprint of predicting with model

UPLOAD_FOLDER = 'upload'  # Save images in folder upload
ALLOWED_EXTENSIONS = {'jpg', 'jpeg'}  # Only accept two types of image extension
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001, debug=True)


