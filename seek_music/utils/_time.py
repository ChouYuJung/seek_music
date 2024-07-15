import contextlib
import time


@contextlib.contextmanager
def delay(delay_time: float | int):
    time.sleep(delay_time)
    yield
