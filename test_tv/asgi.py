import os

import channels.asgi


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "test_tv.settings")
channel_layer = channels.asgi.get_channel_layer()
