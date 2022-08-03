from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
          'author': { 'username': 'John'},
          'body': 'Beautifull day in Portland'
        },
        {
          'author': { 'username': 'Susan'},
          'body': 'The Avenger movie was so cool!'
        },
    ]
    return render_template('index.html', user=user, posts=posts)