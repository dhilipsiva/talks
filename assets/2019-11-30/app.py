from flask import Flask, request
from flask_opentracing import FlaskTracer

from pinger_pb2 import Request
from utils import get_random_stub, tracer

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello, World!"


@app.route("/ping")
def ping():
    stub = get_random_stub()
    request_id = request.args.get('request_id')
    reply = stub.Ping(Request(request_id=request_id))
    return reply.msg


def initialize_tracer():
    return tracer


flask_tracer = FlaskTracer(initialize_tracer, True, app)
