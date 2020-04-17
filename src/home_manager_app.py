from flask import Flask, render_template
BASE_API_ROUTE = '/api/v1'


def create_app():
    return Flask(__name__)


app = create_app()


@app.route('/index')
@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route(f'{BASE_API_ROUTE}/command')
def run_command():
    pass
