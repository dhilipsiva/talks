import time

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


def wait_for_termination():
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        pass
