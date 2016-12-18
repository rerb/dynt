import time

from .models import TestResult


def ws_connect(message):
    responses = {"/num-failures": TestResult.get_num_failures,
                 "/num-errors": TestResult.get_num_errors,
                 "/num-successes": TestResult.get_num_successes,
                 "/num-left": TestResult.get_num_left}

    while True:
        num = responses[message["path"]]()
        message.reply_channel.send({"text": str(num)})
        time.sleep(1)
