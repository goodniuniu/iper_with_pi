from flask import Flask, request

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    if file:
        filename = secure_filename(file.filename)
        file.save(os.path.join('/path/to/upload/', filename))
        return 'File uploaded successfully'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
