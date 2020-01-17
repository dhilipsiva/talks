from concurrent.futures import ThreadPoolExecutor

import grpc
from django.conf import settings
from django.core.management.base import BaseCommand

from zoogle.zmail.models import Zmail
from zoogle.core.utils import wait_for_termination
from zoogle_pb2 import Mail, Result
from zoogle_pb2_grpc import ZmailServicer, add_ZmailServicer_to_server


class ZmailService(ZmailServicer):

    def Mails(self, void, context):
        zmails = Zmail.objects.all()
        for zmail in zmails:
            yield Mail(
                subject=zmail.subject, description=zmail.description,
                from_addr=zmail.from_addr, to_addr=zmail.to_addr)

    def Search(self, query, context):
        zmails = Zmail.objects.filter(subject__icontains=query.text)
        for zmail in zmails:
            yield Result(subject=zmail.subject, description=zmail.description)


class Command(BaseCommand):
    help = "Zmail Server"

    def handle(self, *args, **options):
        server = grpc.server(ThreadPoolExecutor(max_workers=10))
        add_ZmailServicer_to_server(ZmailService(), server)
        server.add_insecure_port(f'[::]:{settings.ZMAIL_PORT}')
        print(f'Starting zmail server on {settings.ZMAIL_PORT}...')
        server.start()
        wait_for_termination()
        server.stop(0)
