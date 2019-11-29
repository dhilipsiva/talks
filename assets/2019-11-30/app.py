from flask import Flask, request
from flask_opentracing import FlaskTracer

from utils import get_config
from github_pb2 import Request
from gist_client import gist_stub
from repo_client import repo_stub
from account_client import account_stub
from commondb_client import commondb_stub

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello, World!"


@app.route("/account")
def account():
    request_id = request.args.get('request_id')
    req = Request(request_id=request_id)
    commondb_stub.GetCommonData(req)
    reply = account_stub.GetUserName(req)
    return reply.msg


@app.route("/repo")
def repo():
    request_id = request.args.get('request_id')
    req = Request(request_id=request_id)
    commondb_stub.GetCommonData(req)
    reply = repo_stub.GetLatestCommit(req)
    return reply.msg


@app.route("/gist")
def gist():
    request_id = request.args.get('request_id')
    req = Request(request_id=request_id)
    commondb_stub.GetCommonData(req)
    reply = gist_stub.GetPublicGist(req)
    return reply.msg


def initialize_tracer():
    config = get_config('api')
    return config.initialize_tracer()


flask_tracer = FlaskTracer(initialize_tracer, True, app)
