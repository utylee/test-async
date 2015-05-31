import sys
import asyncio
import time

from PyQt5.QtWidgets import QApplication, QProgressBar
from quamash import QThreadExecutor, QEventLoop

app = QApplication(sys.argv)
loop = QEventLoop(app)
asyncio.set_event_loop(loop)

progress = QProgressBar()
progress.setRange(0, 99)
progress.show()


@asyncio.coroutine
def master():
    yield from first_50()
    with QThreadExecutor(1) as exec:
        yield from loop.run_in_executor(exec, last_50)





