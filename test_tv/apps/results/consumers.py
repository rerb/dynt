import time

from .models import TestResult


def ws_connect(message):
    while True:
        num_failures = TestResult.get_num_failures()
        message.reply_channel.send(
            {"text": str(num_failures)})
        time.sleep(1)




