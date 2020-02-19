from flask import Flask

app = Flask(__name__)

from rest.app import routes