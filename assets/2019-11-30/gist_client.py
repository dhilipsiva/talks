from grpc import insecure_channel
from opentracing import global_tracer
from grpc_opentracing.grpcext import intercept_channel
from grpc_opentracing import open_tracing_client_interceptor

from utils import get_config
# from github_pb2 import Request
from github_pb2_grpc import GistStub


config = get_config('gist-client')
tracer = global_tracer()
tracer_interceptor = open_tracing_client_interceptor(
    tracer, log_payloads=True)
channel = insecure_channel('gist:50054')
channel = intercept_channel(channel, tracer_interceptor)
gist_stub = GistStub(channel)
# response = gist_stub.GetPublicGist(Request(request_id='foo'))
# print("Greeter client received: " + response.msg)
