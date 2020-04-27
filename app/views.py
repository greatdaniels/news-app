from flask import render_template
from app import app
from .request import get_sources

#views
@app.route('/')
def index():
    '''
    view root page function returns index page
    '''

    #getting general news
    general = get_sources('general')
    business = get_sources('business')
    sports = get_sources('sports')

    title = 'Home - News from Diverse sources'
    return render_template('index.html', title = title, general = general, business = business, sports = sports)

@app.route('/articles/<id>')
def articles(id):
    '''
    view articles page that returns article details
    '''
    all_articles = articles_source(id)
    source = id
    return render_template('articles.html', articles = all_articles, source = source)