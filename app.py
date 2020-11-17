import json
import os
from flask import Flask, redirect, request, url_for, session
from flask_login import LoginManager, current_user
from user import User
from routeControllers.oauth import oauthPage, login_manager

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

# Flask app setup
app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY") or os.urandom(24)

# User session management setup
login_manager.init_app(app)

app.register_blueprint(oauthPage, url_prefix='/oauth')


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


if __name__ == "__main__":
    # app.run(ssl_context="adhoc", debug=True)
    app.run(debug=True)
