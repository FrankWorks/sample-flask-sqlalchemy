# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

# Flask modules
from flask   import redirect, render_template, request
from jinja2  import TemplateNotFound
import json
# from .models import sqldb

# App modules
from app import app

import sqldb

# Class instanciation
s = sqldb.UserList()
# Retrieving User Dictionary
u = json.loads(sqldb.UserList.listUser(s))

# App main route + generic routing
# @app.route('/', defaults={'path': 'index.html'})
@app.route('/', defaults={'path': 'DPRData.html'})
@app.route('/<path>')
def index(path):

    try:

        # Detect the current page
        segment = get_segment( request )

        # Serve the file (if exists) from app/templates/FILE.html
        return render_template( path, segment=segment )
    
    except TemplateNotFound:
        return render_template('page-404.html'), 404

# Helper - Extract current page name from request 
def get_segment( request ): 

    try:

        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment    

    except:
        return None 
@app.route('/Office365Login',methods=["GET", "POST"])
def Office365Login():
    print('In SomeFunction')
    # return "Nothing"
    return redirect('/Office365Login.html')

@app.route('/DPRData',methods=["GET", "POST"])
def DPRData():
    # return render_template('DPRData.html',items = s)
    return render_template('DPRData.html',items = u)