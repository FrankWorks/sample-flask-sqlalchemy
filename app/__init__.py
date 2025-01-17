# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

# Import core packages
import os
import sys

# Import Flask 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate    import Migrate
from DPR.gem import gem_bp


sys.path.append('./app/models')
# Inject Flask magic
app = Flask(__name__)
# app.config['DEBUG'] = True
# Load configuration
app.config.from_object('app.config.Config')

# Construct the DB Object (SQLAlchemy interface)
db = SQLAlchemy (app)

# Enabel migration for our application
Migrate(app, db)

# Import routing to render the pages
from app import views, models

app.register_blueprint(gem_bp)
