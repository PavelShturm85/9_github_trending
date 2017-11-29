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


def print_open_issues(issues, repositories):
    for number_repository, repository in enumerate(repositories, 1):
        print('repository №{}, name:{}:'.format(
            number_repository, repository['name']))
        # Because the numbering in the list begins with [0], so we use -1.
        for number_issue, issue in enumerate(issues[number_repository-1], 1):
            print('open issue:{} \t {}'.format(
                number_issue, issue['url']))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        input_amount = sys.argv[1]
    else:
        input_amount = 10
    repositories = get_trending_repositories(input_amount)
    issues = get_open_issues(repositories)
    print_open_issues(issues, repositories)
