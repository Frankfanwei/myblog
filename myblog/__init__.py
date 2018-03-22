from flask import Flask
from flask import render_template

app=Flask(__name__)
#app.config.from_object(__name__)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/blog/')
def blog():
    return render_template('blog.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')


