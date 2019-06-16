import os
from flask import Flask, flash, request, redirect, url_for, jsonify, session
from werkzeug.utils import secure_filename
from src.image_parser import ImageDealer
import time
import hashlib

id = ImageDealer()

# UPLOAD_FOLDER = '/home/ubuntu/photos'
UPLOAD_FOLDER = '../web/photos'
SECRET_KEY = 'bd28cba11f1b754d22e09977fb48b47a'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# app.secret_key = SECRET_KEY

app = Flask(__name__)

def getHash():
  hash = hashlib.sha1()
  hash.update(str(time.time()).encode('utf-8'))
  return hash.hexdigest()[:10]

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# def rotateImage(rotate, path):
#   im1 = Image.open(path)
#   im2 = im1.rotate(rotate)
#   im2.save(path)

@app.route('/api/upload', methods=["POST"])
def upload():
  if 'the_file' not in request.files:
    flash('No file part')
    return redirect("/")

  file = request.files["the_file"]
  rotate = request.form["rotate"]
  if file.filename == '':
    flash('No selected files')
    return redirect('/')
  if file and allowed_file(file.filename):
    filename = getHash() + secure_filename(file.filename)
    fullpath = os.path.join(UPLOAD_FOLDER, filename)
    file.save(fullpath)
    # rotateImage(rotate, fullpath)
    print("request rotate = " + rotate)
    predict = id.parse_image(UPLOAD_FOLDER, filename, rotate)
    return jsonify(predict)

if __name__ == "__main__":
    app.secret_key = SECRET_KEY
    app.debug = False
    app.run(host='0.0.0.0')