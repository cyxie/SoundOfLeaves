from flask import render_template
app = Flask(__name__)

@app.route("/")
def index():
    return 'Index'

@app.route('/hello')
def hello():
    return 'Hello'

if __name__ == '__main__':
    app.run()