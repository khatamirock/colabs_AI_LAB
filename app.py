import os
from flask import Flask, jsonify, request, url_for, redirect, render_template, session
import requests
import DT
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ronin-Rock'

ALLOWED_EXTENSION = set(['csv'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1).lower() in ALLOWED_EXTENSION


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        print(file)
        # if file and allowed_file(file.filename):

    strr = DT.callmeDt(file)
    print(strr)
    return render_template('index.html', datas='kire')


@app.route('/')
def index():

    # print(str(strr))
    return render_template('index.html', datas='kire')


if __name__ == '__main__':

    app.run(debug=True)
