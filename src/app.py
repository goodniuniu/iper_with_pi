from flask import Flask, render_template, url_for
import os
import json

app = Flask(__name__)

@app.route('/')
def index():
    files = os.listdir('data')  # 假设您的文件都在upload目录下
    return render_template('index.html', files=files)

@app.route('/analyze/<filename>')
def analyze(filename):
    # 这里添加解析文件的代码，提取有价值的数据
    filepath = os.path.join('upload', filename)
    with open(filepath, 'r') as file:
        data = json.load(file)
        # 提取所需信息的逻辑
    return render_template('analysis.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
