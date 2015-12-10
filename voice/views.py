from voice import app
from flask import request, render_template, jsonify
import ujson
import tempfile
import shutil
import os

@app.route('/')
def index():
    return render_template('index.html', key=None)

@app.route('/submit', methods=['POST'])
def submit():
    dirpath = tempfile.mkdtemp();
    path = os.path.join(dirpath, 'audio.wav')
    request.files['blob'].save(path)

    # TODO: process the wav file save at path
    size = os.path.getsize(path)



    shutil.rmtree(dirpath)

    # TODO: return the result
    return jsonify({
        'size': size
    });
