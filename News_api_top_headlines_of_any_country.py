import requests

def get_news(country, api_key='d8e89bc5525f49f9879e0a1b6292c664'):
    url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={api_key}'
    r = requests.get(url)
    content = r.json()
    articles = content['articles']
    result = []

    for article in articles:
        result.append(f"TITLE: {article['title']} 'DESCRIPTION:' {article['description']}")
    
    print(result)

get_news(country='us')