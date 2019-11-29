from random import choice

from jaeger_client import Config
from grpc import insecure_channel
from grpc_opentracing.grpcext import intercept_channel
from grpc_opentracing import open_tracing_client_interceptor

from pinger_pb2_grpc import PingerStub
from config import PORT, HOSTS, SERVICE_NAME

config = Config(
    config={
        'sampler': {
            'type': 'const',
            'param': 1,
        },
        'local_agent': {
            'reporting_host': '192.168.99.109',
            'reporting_port': '6831',
        },
        'logging': True,
    },
    service_name=SERVICE_NAME)
tracer = config.initialize_tracer()


def get_random_stub():
    # No Idea how to close this tracer for now.
    # Will leave it open for demo purpose :P
    # config = get_jaeger_config()
    tracer_interceptor = open_tracing_client_interceptor(
        tracer, log_payloads=True)
    host = choice(HOSTS)
    connection = f'{host}:{PORT}'
    channel = insecure_channel(connection)
    channel = intercept_channel(channel, tracer_interceptor)
    # No Idea how to close this channel for now.
    # Will leave it open for demo purpose :P
    return PingerStub(channel)
