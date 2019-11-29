from random import choice

from grpc import insecure_channel

from config import PORT, HOSTS
from pinger_pb2_grpc import PingerStub


def get_random_stub():
    # Ugly temp hack for demo
    host = choice(HOSTS)
    connection = f'{host}:{PORT}'
    channel = insecure_channel(connection)
    # No Idea how to close this channel for now.
    # Will leave it open for demo purpose :P
    return PingerStub(channel)
