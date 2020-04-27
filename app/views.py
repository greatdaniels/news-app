from flask import render_template, request, url_for
from app import app
from .request import get_sources, get_articles

#views
@app.route('/')
def index():
    '''
    view root page function returns index page
    '''

    #getting news
    general = get_sources('general')
    business = get_sources('business')
    sports = get_sources('sports')
    technology = get_sources('technology')
    science = get_sources('science')

    title = 'Home - News from Diverse sources'
    return render_template('index.html', title = title, general = general, business = business, sports =sports, tech = technology, science = science)

@app.route('/articles/<article>')
def articles(article):
    '''
    view articles page that returns article details
    '''
    all_articles = get_articles(article)

    title = f'{article}'
    return render_template('articles.html', title = title, articles = all_articles, name =f'{article}')