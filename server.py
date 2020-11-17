import json
import os
from flask import Flask, redirect, request, url_for, session, render_template
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
    return render_template("index.html.j2")


if __name__ == "__main__":
    # app.run(ssl_context="adhoc", debug=True)
    app.run(debug=True)
