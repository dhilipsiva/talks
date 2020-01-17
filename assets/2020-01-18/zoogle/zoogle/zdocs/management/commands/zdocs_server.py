from concurrent.futures import ThreadPoolExecutor

import grpc
from django.conf import settings
from django.core.management.base import BaseCommand

from zoogle.zdocs.models import Zdoc
from zoogle.core.utils import wait_for_termination
from zoogle_pb2 import Doc, Result
from zoogle_pb2_grpc import ZdocsServicer, add_ZdocsServicer_to_server


class ZdocsService(ZdocsServicer):

    def Docs(self, void, context):
        zdocs = Zdoc.objects.all()
        for zdoc in zdocs:
            yield Doc(
                subject=zdoc.subject, description=zdoc.description,
                owner=zdoc.owner, size=zdoc.size)

    def Search(self, query, context):
        zdocs = Zdoc.objects.filter(subject__icontains=query.text)
        for zdoc in zdocs:
            yield Result(subject=zdoc.subject, description=zdoc.description)


class Command(BaseCommand):
    help = "Zdocs Server"

    def handle(self, *args, **options):
        server = grpc.server(ThreadPoolExecutor(max_workers=10))
        add_ZdocsServicer_to_server(ZdocsService(), server)
        server.add_insecure_port(f'[::]:{settings.ZDOCS_PORT}')
        print(f'Starting zdoc server on {settings.ZDOCS_PORT}...')
        server.start()
        wait_for_termination()
        server.stop(0)
