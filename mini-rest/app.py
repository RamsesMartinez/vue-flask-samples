import os
from flask import Flask, flash, request, redirect, render_template, Response, jsonify
from flask_cors import CORS

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
DEBUG = True
PORT = 5000
app = Flask(__name__)
app.secret_key = os.urandom(24)
cors = CORS(app, resources={r"/api/file": {"origins": "*"}})


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def upload_form():
    return render_template('upload.html')


@app.route('/api/file', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        
        # check if the post request has the file part
        if 'file' not in request.files:
            print('no file...')
            flash('No file part')
            return jsonify({
                'msg': 'No file'
            })
        file = request.files['file']
        
        if file.filename == '':
            flash('No file selected for uploading')
            return redirect(request.url)

        else:
            flash('Allowed file types are txt, pdf, png, jpg, jpeg, gif')
            return redirect(request.url)


if __name__ == "__main__":
    app.run(port=PORT, debug=DEBUG)
