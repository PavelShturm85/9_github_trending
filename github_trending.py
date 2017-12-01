import requests
import datetime
import sys


def get_trending_repositories(top_size):
    date_now = datetime.datetime.now()
    last_week = (date_now - datetime.timedelta(days=7)).strftime('%Y-%m-%d')
    filter_params = dict(
        q='created:>{}'.format(last_week),
        sort='stars',
        order='desc',
        page='1',
        per_page=top_size,
    )
    url = 'https://api.github.com/search/repositories'
    repositories = requests.get(url, params=filter_params).json()['items']
    return repositories


def get_open_issues(repositories):
    issues = []
    for repository in repositories:
        url = 'https://api.github.com/repos/{}/issues'.format(
            repository['full_name'])
        issues.append(requests.get(url).json())
    return issues


def print_issues_amount(issues, repositories):

    for number, (repository, issue) in enumerate(zip(repositories, issues), 1):
            print('{}) Progect name: {} \t amount issues:{} \t {}'.format(
                number,
                repository['name'],
                len(issue),
                repository['html_url']
            ))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        input_amount = sys.argv[1]
    else:
        input_amount = 10
    repositories = get_trending_repositories(input_amount)
    issues = get_open_issues(repositories)
    print_issues_amount(issues, repositories)
