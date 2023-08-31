# app.py

from flask import Flask, render_template
from flask_assets import Bundle, Environment

app = Flask(__name__)

assets = Environment(app)
css = Bundle("src/main.css", output="dist/main.css")
js = Bundle("src/*.js", output="dist/main.js")  # new

assets.register("css", css)
assets.register("js", js)  # new
css.build()
js.build()  # new


@app.route("/")
def homepage():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
