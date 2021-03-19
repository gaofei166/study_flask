from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    print("=========执行index============")
    mstr = '测试测试测试'
    mint = '开会开会开会'
    return render_template('index.html', my_str=mstr, my_int=mint)


if __name__ == '__main__':
    app.run(host='', port=5000, debug=True)