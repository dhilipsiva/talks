from concurrent.futures import ThreadPoolExecutor

import grpc
from grpc_opentracing.grpcext import intercept_server
from grpc_opentracing import open_tracing_server_interceptor

from github_pb2 import Reply
from utils import get_config, wait_for_termination
from github_pb2_grpc import GistServicer, add_GistServicer_to_server
from codedb_client import codedb_stub


class Gist(GistServicer):

    def GetPublicGist(self, request, context):
        codedb_stub.GetCodeData(request)
        return Reply(msg='gist')


def serve():
    config = get_config('gist-server')
    tracer = config.initialize_tracer()
    tracer_interceptor = open_tracing_server_interceptor(
        tracer, log_payloads=True)
    server = grpc.server(ThreadPoolExecutor(max_workers=10))
    server = intercept_server(server, tracer_interceptor)
    add_GistServicer_to_server(Gist(), server)
    server.add_insecure_port('[::]:50054')
    server.start()
    wait_for_termination()
    server.stop(0)
    tracer.close()


if __name__ == '__main__':
    serve()
