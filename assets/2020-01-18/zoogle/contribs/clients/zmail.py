from grpc import insecure_channel
from django.conf import settings
from zoogle_pb2_grpc import ZmailStub


channel = insecure_channel(f'localhost:{settings.ZMAIL_PORT}')
zmail_stub = ZmailStub(channel)
