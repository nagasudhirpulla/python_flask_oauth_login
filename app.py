# Python standard libraries
import json
import os
import sqlite3

# Third party libraries
from flask import Flask, redirect, request, url_for, session
from flask_login import (
    LoginManager,
    current_user,
    login_required,
    login_user,
    logout_user,
)

from user import User
from routeControllers.oauth import oauthPage


os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
# print this using
# print(os.environ['OAUTHLIB_INSECURE_TRANSPORT'])


# Flask app setup
app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY") or os.urandom(24)

# User session management setup
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.unauthorized_handler
def unauthorized():
    return "You must be logged in to access this content.", 403


# Flask-Login helper to retrieve a user from our db
@login_manager.user_loader
def load_user(user_id):
    sUser = session['SUSER']
    return User(sUser['id'], sUser['name'], sUser['email'])


@app.route("/")
def index():
    if current_user.is_authenticated:
        return (
            "<p>Hello, {}! You're logged in! Email: {}</p>"
            '<a class="button" href="/oauth/logout">Logout</a>'.format(
                current_user.name, current_user.email
            )
        )
    else:
        return '<a class="button" href="/oauth/login">Login</a>'


app.register_blueprint(oauthPage, url_prefix='/oauth')


if __name__ == "__main__":
    # app.run(ssl_context="adhoc", debug=True)
    app.run(debug=True)
