from grpc import insecure_channel
from opentracing import global_tracer
from grpc_opentracing.grpcext import intercept_channel
from grpc_opentracing import open_tracing_client_interceptor

# from utils import get_config
# from github_pb2 import Request
from github_pb2_grpc import AccountStub


# config = get_config('account-client')
tracer = global_tracer()
tracer_interceptor = open_tracing_client_interceptor(
    tracer, log_payloads=True)
channel = insecure_channel('localhost:50051')
channel = intercept_channel(channel, tracer_interceptor)
account_stub = AccountStub(channel)
# response = account_stub.GetUserName(Request(request_id='foo'))
# print("Greeter client received: " + response.msg)
