from flask import Flask, request
from flask_opentracing import FlaskTracer

from utils import get_config
from github_pb2 import Request
from account_client import account_stub

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello, World!"


@app.route("/ping")
def ping():
    request_id = request.args.get('request_id')
    reply = account_stub.GetUserName(Request(request_id=request_id))
    return reply.msg


def initialize_tracer():
    config = get_config('api')
    return config.initialize_tracer()


flask_tracer = FlaskTracer(initialize_tracer, True, app)
