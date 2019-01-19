"""

Usage:

Windows: set FLASK_APP=name-of-the-file.py(doar cmd)
         flask run

Linux: extract FLASK_APP=name-of-the-file.py
         flask run

"""


from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def hello():
    return 'hey'
