import requests
from invoke import task


def _ping(endpoint):
    r = requests.get(f'http://127.0.0.1:5000/{endpoint}')
    print(r.text)


@task
def account(c):
    _ping('account')


@task
def repo(c):
    _ping('repo')


@task
def gist(c):
    _ping('gist')
