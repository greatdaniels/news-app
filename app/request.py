from app import app
import urllib.request, json
from .models import sources

Sources = sources.Sources

#getting api key

api_key = app.config['NEWS_API_KEY']

#getting the news base url

base_url = app.config['NEWS_API_BASE_URL']

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
