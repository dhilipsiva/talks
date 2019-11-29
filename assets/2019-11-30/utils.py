import time
from jaeger_client import Config

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


def get_config(service_name):
    return Config(
        config={
            'sampler': {
                'type': 'const',
                'param': 1,
            },
            'local_agent': {
                # 'reporting_host': '192.168.99.109',
                'reporting_host': 'jaeger',
                'reporting_port': '6831',
            },
            'logging': True,
        },
        service_name=service_name)


def wait_for_termination():
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        pass
