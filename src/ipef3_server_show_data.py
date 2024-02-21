from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def show_results():
    results = []
    with open("iperf_results.json", "r") as file:
        for line in file:
            results.append(json.loads(line))
    # 使用 render_template 显示结果，这里假设你有一个名为 'results.html' 的模板
    return render_template('results.html', results=results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
