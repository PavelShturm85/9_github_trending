import requests
import datetime
import sys


def get_trending_repositories(top_size):
    date_now = datetime.datetime.now()
    last_week = (date_now - datetime.timedelta(days=7)).strftime('%Y-%m-%d')

    filter_params = {'sort': 'stars',
                     'order': 'desc',
                     'page': '1'}
    filter_params['q'] = 'created:>{}'.format(last_week)
    filter_params['per_page'] = '{}'.format(top_size)
    url = 'https://api.github.com/search/repositories'
    repositories = requests.get(url, params=filter_params).json()['items']
    return repositories


def print_open_issues_amount(repositories):
    for number_repository, repository in enumerate(repositories, 1):
        url = 'https://api.github.com/repos/{}/issues'.format(
            repository['full_name'])
        issues = requests.get(url).json()
        print('repository №{}, name:{}:'.format(
            number_repository, repository['name']))
        for number_issue, issue in enumerate(issues, 1):
            print('open issue:{} \t {}'.format(
                number_issue, issue['url']))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        input_amount = sys.argv[1]
    else:
        input_amount = input('Enter amount repositories: ')
    filter_repositories = get_trending_repositories(input_amount)
    print_open_issues_amount(filter_repositories)
