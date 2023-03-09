from flask import Flask
from flask import render_template
from flask import __version__
import os
import sys 
sys.path.append('..')

from gem import gem_bp
# from Gem.gem import gem_bp

STATIC_DIR = os.path.join(os.path.dirname(__file__), 'static')

app = Flask(__name__, static_folder=STATIC_DIR)

@app.route('/')

def home():
    # return "DPR Web Site"
    return render_template('home.html')

@app.route('/about/')

def about():
    # return "DPR About"
    return render_template('about.html')
    
@app.route('/login/')

def login():
    # return "DPR About"
    return render_template('login.html')    

# app.register_blueprint(gem_bp)
if __name__=='__manin__':
    app.run(debug=True)