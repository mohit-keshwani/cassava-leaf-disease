import numpy as np
import boto3
import flask
from flask import Flask, request, jsonify, render_template
import pandas as pd
from werkzeug.utils import secure_filename
import re
import json
import os
import tensorflow as tf 
from time import time
from PIL import Image

import warnings
warnings.filterwarnings('ignore')

app = Flask(__name__)
s3 = boto3.resource(service_name = 's3',
                   region_name = 'REGION-NAME',
                   aws_access_key_id = 'ACCESS-KEY-ID',
                   aws_secret_access_key = 'SECRET-ACCESS-KEY')

model1 = tf.keras.models.load_model("Model1.h5")
model3 = tf.keras.models.load_model("Model2.h5")

class_dict = {0: "Cassava Bacterial Blight (CBB)",
              1: "Cassava Brown Streak Disease (CBSD)",
              2: "Cassava Green Mottle (CGM)",
              3: "Cassava Mosaic Disease (CMD)",
              4: "Healthy"}


@app.route('/')
def home():
    return render_template('Index.html')

@app.route('/predict' , methods = ['POST','GET'])

def predict():
    if request.method == 'POST':
        try:
            if 'image' in request.files:
                model1_list = []
                model3_list = []
                img = request.files['image']
                filename = secure_filename(img.filename)
                img.save(filename)
                s3.Bucket('cassava-leaf-disease').upload_file(Filename= filename, Key= "Images/"+filename)
                img = Image.open(filename)
                test_image = np.asarray(img)
                test_image = tf.cast(test_image , tf.float32)
                test_image = tf.image.resize(test_image , (224 , 224)) 
                test_image = test_image/255
                test_image = test_image.numpy()
                processed_test_image = np.expand_dims(test_image, axis = 0)
                model1_list.append(model1.predict(processed_test_image))
                model3_list.append(model3.predict(processed_test_image))
                for mob, dense in zip(model1_list, model3_list):
                    pred = np.argmax(mob/np.linalg.norm(mob) + dense/np.linalg.norm(dense))
            return render_template('Index.html', result = class_dict[pred])
        except:
            message = "Please upload an Image"
            return render_template('Index.html', result = message)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
  