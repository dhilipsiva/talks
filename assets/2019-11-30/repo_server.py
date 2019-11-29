from concurrent.futures import ThreadPoolExecutor

import grpc
from grpc_opentracing.grpcext import intercept_server
from grpc_opentracing import open_tracing_server_interceptor

from github_pb2 import Reply
from utils import get_config, wait_for_termination
from github_pb2_grpc import RepoServicer, add_RepoServicer_to_server
from codedb_client import codedb_stub


class Repo(RepoServicer):

    def GetLatestCommit(self, request, context):
        codedb_stub.GetCodeData(request)
        return Reply(msg='repo')


def serve():
    config = get_config('repo-server')
    tracer = config.initialize_tracer()
    tracer_interceptor = open_tracing_server_interceptor(
        tracer, log_payloads=True)
    server = grpc.server(ThreadPoolExecutor(max_workers=10))
    server = intercept_server(server, tracer_interceptor)
    add_RepoServicer_to_server(Repo(), server)
    server.add_insecure_port('[::]:50055')
    server.start()
    wait_for_termination()
    server.stop(0)
    tracer.close()


if __name__ == '__main__':
    serve()
