import requests
import json
import datetime


def get_trending_repositories():
    date_now = datetime.datetime.now()
    before_week = (date_now - datetime.timedelta(days=7)).strftime('%Y-%m-%d')

    filter_params = {'sort': 'stars',
                     'order': 'desc',
                     'page': '1',
                     'per_page': '20'}
    preload['q'] = 'created:>{}'.format(before_week)
    url = 'Https://api.github.com/search/repositories'
    repositories = (requests.get(url, params=filter_params)).json()['items']
    return repositories


def print_open_issues_and_url(repositories):
    for number, repo in enumerate(repositories, 1):
        print('{}) \t open issues:{} \t {}'.format(
            number, repo['open_issues'], repo['url']))


if __name__ == '__main__':
    print_open_issues_and_url(get_trending_repositories())
