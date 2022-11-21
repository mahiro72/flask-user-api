from flask import Flask
from presentation.router import user

app = Flask(__name__)
app.register_blueprint(user.api)

