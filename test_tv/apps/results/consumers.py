from .models import TestResult


REPLY_CHANNELS = {"num_failures": None}


def _send_num_failures():
    num_failures = TestResult.get_num_failures()
    REPLY_CHANNELS["num_failures"].send(
        {"text": str(num_failures)})


# Listens on num-failures (Supposedly.)
def num_failures(message):
    import ipdb; ipdb.set_trace()
    _send_num_failures()


def ws_connect(message):
    import ipdb; ipdb.set_trace()
    REPLY_CHANNELS["num_failures"] = message.reply_channel
    _send_num_failures()


def ws_receive(message):
    import ipdb; ipdb.set_trace()
    _send_num_failures()


def update_num_failures():
    _send_num_failures()
