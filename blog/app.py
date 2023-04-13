from flask import Flask, render_template
from blog.report.views import report
from blog.user.views import user
from blog.views.users import users_app
from blog.views.articles import articles_app


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


def create_app() -> Flask:
    app = Flask(__name__)
    register_blueprints(app)
    return app


def register_blueprints(app: Flask):
    app.register_blueprint(user)
    app.register_blueprint(report)
    app.register_blueprint(users_app, url_prefix="/users")
    app.register_blueprint(articles_app, url_prefix="/articles")
