from flask import Flask, render_template, url_for, send_file
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/img/<filename>.jpg')
def sendImg(filename):
    return send_file('./img/'+ str(filename) + '.jpg')

app.run(host="localhost", port=5000)