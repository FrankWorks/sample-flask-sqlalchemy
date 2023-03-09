from flask import Blueprint, render_template
from flask import Flask
from flask import render_template
from flask import __version__
import os
import sys 

# STATIC_DIR = os.path.join(os.path.dirname(__file__), 'static')
gem_bp =Blueprint('gem_bp', __name__, template_folder='templates', static_folder='static', url_prefix='/gem')

@gem_bp.route('/')

def home():
    return "DPR Web Site"
    # return render_template('gem/home.html')

@gem_bp.route('/about/')

def about():
    return "DPR About"
    # return render_template('gem/about.html')
    
@gem_bp.route('/login/')

def login():
    return "DPR About"
    # return render_template('gem/login.html')    
