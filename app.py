from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
import time,json,re,os

UPLOAD_FOLDER = 'input/tempData/'
ALLOWED_EXTENSIONS = set(['txt'])

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/dashboard")
def dashboard():
    return render_template('dashboard.html')

@app.route("/input_barang")
def input_barang():
    return render_template('formbarang.html')

@app.route("/input_rak")
def input_rak():
    return render_template('formrak.html')

@app.route("/penempatan")
def penempatan():
    return render_template('penempatan.html')

@app.route("/process")
def process():
    return "Maaf sistem sedang dalam tahap pembangunan, silahkan coba di lain waktu"

if __name__ == "__main__":
    port = int(os.environ.get("PORT",5000))
    app.run(host="0.0.0.0",port=port)
