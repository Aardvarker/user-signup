#!/usr/bin/env python
from flask import Flask, request
import os
import jinja2

templates_dr = os.path.join(os.path.dirname(__file__),'templates')
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(templates_dr))

app = Flask(__name__)
app.config['DEBUG'] = True



@app.route("/")
def index():
    template = jinja_env.get_template('user_signup_template.html')
    return template.render()

if __name__=='__main__':
    app.run()