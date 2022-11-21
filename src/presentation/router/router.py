from flask import Flask

from presentation.router import user
from presentation.router import health


app = Flask(__name__)

app.register_blueprint(health.api)
app.register_blueprint(user.api)
