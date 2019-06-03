# register blue-prints here

from flask import Flask
from app import views

# Initialize application
app = Flask(__name__, static_folder=None)

app.register_blueprint(views.app_route)





