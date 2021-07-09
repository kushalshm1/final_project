from logging import debug
from flask import Flask, request, render_template, url_for
import numpy as np
import re
import matplotlib.pyplot as plt
import cv2
from main import classify
app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def get():
    sign = "Turn Left"
    if request.method == 'POST':
        data = request.get_data()
        data = data.decode('utf-8')
        # print(data)
        data = re.findall(r'\d+', data)
        data = np.array(data).reshape(80,80,3).astype(np.uint8)
        img = cv2.cvtColor(data, cv2.COLOR_RGB2BGR)
        plt.imsave(url_for('static',filename='cam.jpg'),img)
        sign = classify(url_for('static',filename='cam.jpg'))
    return render_template('index.html',sign=sign)
if __name__=='__main__':
    app.run(debug=True)