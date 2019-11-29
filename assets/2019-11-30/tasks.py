import requests
from invoke import task
import opentelemetry.ext.http_requests
from opentelemetry.trace import tracer

opentelemetry.ext.http_requests.enable(tracer())


@task
def ping(c, n=1):
    for i in range(n):
        r = requests.get(f'http://127.0.0.1:5000/ping?request_id={i}')
        print(r.text)
