from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main():
    return render_template('main.html')

@app.route('/hoge')
def hoge():
    return render_template('hoge.html')

if __name__ == '__main__':
    app.debug = True
    app.run()