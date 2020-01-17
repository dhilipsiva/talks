from grpc import insecure_channel
from django.conf import settings
from zoogle_pb2_grpc import ZdocsStub


channel = insecure_channel(f'localhost:{settings.ZDOCS_PORT}')
zdocs_stub = ZdocsStub(channel)
