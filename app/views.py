from flask import render_template
from app import app

#views
@app.route('/')
def index():
    '''
    view root page function returns index page
    '''
    title = 'Home - News from Diverse sources'
    return render_template('index.html', title = title)

@app.route('/articles/<id>')
def articles(id):
    '''
    view articles page that returns article details
    '''
    return render_template('articles.html', id = id)