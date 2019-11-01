import os
import sys
import flask
folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, folder)


from boolog.infrastructure.view_modifiers import response

app = flask.Flask(__name__)


def get_latest_blog_posts():
    return [
        {"id": 0, "name": "test1", "date": "friday"},
        {"id": 1, "name": "test2", "date": "tuesday"},
    ]


@app.route("/")
@response(template_file='home/index.html')
def index():
    _blog = get_latest_blog_posts()
    return {'posts': _blog}


@app.route("/about")
@response(template_file='home/about.html')
def about():
    return {}


if __name__ == "__main__":
    app.run(debug=True)
