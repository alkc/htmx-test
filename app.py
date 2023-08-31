# app.py

import time

from flask import Flask, render_template, request
from flask_assets import Bundle, Environment

from todo import todos

# import config


def get_app():
    app = Flask(__name__)

    # app.config.from_object(config.DefaultConfig())  # Note initialization of Config

    assets = Environment(app)
    css = Bundle("src/main.css", output="dist/main.css")
    js = Bundle("src/*.js", output="dist/main.js")

    assets.register("css", css)
    assets.register("js", js)
    css.build()
    js.build()

    return app


app = get_app()


@app.route("/")
def homepage():
    return render_template("index.html")


@app.route("/search", methods=["POST"])
def search_todo():
    search_term = request.form.get("search")

    if not len(search_term):
        return render_template("todo.html", todos=[])

    res_todos = []
    for todo in todos:
        if search_term in todo["title"]:
            res_todos.append(todo)

    return render_template("todo.html", todos=res_todos)


@app.route("/table")
def table_view():
    return render_template("table.html")


@app.route("/button_indicator_test")
def clicked_button():
    time.sleep(2)
    return "<p class='text-center'>congratulations, you clicked buttan!</p>"


@app.route("/indicator")
def indicator_view():
    return render_template("indicator.html")


if __name__ == "__main__":
    app.run(debug=True)
