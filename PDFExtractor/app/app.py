
from flask import Flask, render_template, request, flash, redirect, url_for

import services


app = Flask(__name__)
app.secret_key = '(TS0?SN}lZX}"hRd++1W4nj_sg*Zg0dp'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    
    if 'file' not in request.files:
        flash('No file part', 'error')
        return redirect(url_for('index'))

    file = request.files['file']

    if file.filename == '':
        flash('No selected file', 'error')
        return redirect(url_for('index'))

    # Upload file to S3 bucket
    result = services.upload_to_s3(file)

    if result:
        flash('File uploaded successfully', 'success')
    else:
        flash('File upload failed', 'error')

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()
