from os import environ
PORT = int(environ.get('PORT'))
HOST = environ.get('HOST')
HOSTS = environ.get('HOSTS').split(',')
SERVICE_NAME = environ.get('SERVICE_NAME')

CONNECTION = f'{HOST}:{PORT}'
