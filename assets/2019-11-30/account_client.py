from grpc import insecure_channel
from opentracing import global_tracer
from grpc_opentracing.grpcext import intercept_channel
from grpc_opentracing import open_tracing_client_interceptor

from github_pb2_grpc import AccountStub


tracer = global_tracer()
tracer_interceptor = open_tracing_client_interceptor(
    tracer, log_payloads=True)
channel = insecure_channel('account:50051')
channel = intercept_channel(channel, tracer_interceptor)
account_stub = AccountStub(channel)
