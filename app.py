import os
from flask import Flask,render_template
from werkzeug.contrib.fixers import ProxyFix


app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")
app.wsgi_app = ProxyFix(app.wsgi_app)


if __name__ == "__main__":
    port = int(os.environ.get("PORT",5000))
    app.run(host="127.0.0.1",port=port)
