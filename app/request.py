import urllib.request, json
from .models import Sources, Articles
from datetime import datetime

api_key = None
articles_url = None
base_url = None

def configure_request(app):
    global api_key, base_url, articles_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']
    articles_url = app.config['NEWS_ARTICLES_API_URL']

def get_sources(category):
    '''
    function that gets json response to our url request
    '''
    get_sources_url = base_url.format(category, api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results = process_results(sources_results_list)

    return sources_results

def process_results(sources_list):
    '''
    function that processes the sources results and transform them to a list of objects
    '''
    sources_results = []
    for source_item in sources_list:
        id = source_item.get('id')
        category = source_item.get('category')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        language = source_item.get('language')
        country = source_item.get('country')

        if url:
            source_object = Sources(id, name, description, url, category, language, country)
            sources_results.append(source_object)

    return sources_results

def get_articles(article):
    '''
    function to get articles
    '''
    get_articles_url = articles_url.format(article, api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        articles_data = url.read()
        articles_response = json.loads(articles_data)

        articles_results = None

        if articles_response['articles']:
            articles_results_list = articles_response['articles']
            articles_results = process_articles(articles_results_list)
    
    return articles_results

def process_articles(articles_list):
    '''
    function that processes the json results for the articles
    '''
    articles_results = []

    for article in articles_list:
        source = article.get('source')
        author = article.get('author')
        description = article.get('description')
        title = article.get('title')
        url = article.get('url')
        urlToImage = article.get('urlToImage')
        date_published = article.get('publishedAt')

        publishedAt = datetime(year=int(date_published[0:4]), month=int(date_published[5:7]), day=int(date_published[8:10]), hour=int(date_published[11:13]), minute=int(date_published[14:16]))

        if urlToImage:
            article_object = Articles(source, author, title, description, url, urlToImage, publishedAt)
            articles_results.append(article_object)

    return articles_results
