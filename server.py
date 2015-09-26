import os
import tempfile
from flask import Flask, request, Response

import ocr

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            path = os.path.join(tempfile.gettempdir(), file.filename)
            file.save(path)
            return Response(ocr.main(path), mimetype='text/plain')
    return '''
        <!doctype html>
        <title>ocr test</title>
        <form action="" method=post enctype=multipart/form-data>
            <p><input type=file name=file></p>
            <p><input type=submit value=Upload></p>
        </form>
    '''

if __name__ == '__main__':
    app.run()