from flask import render_template
from . import api


@api.route('/')
def get_home():
    return render_template('index.html')
