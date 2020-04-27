from flask import render_template
from app import app
from .request import get_sources, get_articles

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
    entertainment = get_sources('entertainment')
    technology = get_sources('technology')
    health = get_sources('health')
    science = get_sources('science')

    title = 'Home - News from Diverse sources'
    return render_template('index.html', title = title, general = general, business = business, sports =sports, tech = technology, science = science, health = health)

@app.route('/articles/<id>')
def articles(id):
    '''
    view articles page that returns article details
    '''
    all_articles = get_articles(id)
    articles = id

    title = f'{articles} | All Articles'
    return render_template('articles.html', title = title, articles = all_articles, source = articles )