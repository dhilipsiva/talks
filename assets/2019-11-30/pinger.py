import logging
from concurrent.futures import ThreadPoolExecutor

import grpc

from pinger_pb2 import Reply
from utils import get_random_stub
from config import PORT, SERVICE_NAME
from pinger_pb2_grpc import PingerServicer, add_PingerServicer_to_server

ADDRESS = f'[::]:{PORT}'


class Pinger(PingerServicer):

    @property
    def _stub(self):
        return get_random_stub()

    def LevelTwo(self, request, context):
        print(request, context)
        return Reply(msg=f' <=> (2){SERVICE_NAME}')

    def LevelOne(self, request, context):
        print(request, context)
        reply = self._stub.LevelTwo(request)
        return Reply(msg=f' <=> (1){SERVICE_NAME} {reply.msg}')

    def Ping(self, request, context):
        print(request, context)
        reply = self._stub.LevelOne(request)
        return Reply(
            msg=f'[{request.request_id}] pong {SERVICE_NAME} {reply.msg}')


def serve():
    server = grpc.server(ThreadPoolExecutor(max_workers=10))
    add_PingerServicer_to_server(Pinger(), server)
    print(f'listening on {ADDRESS}...')
    server.add_insecure_port(ADDRESS)
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
