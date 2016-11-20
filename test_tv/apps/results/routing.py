from channels.routing import route


channel_routing = [
    route('websocket.connect',
          'test_tv.apps.results.consumers.ws_connect')
]
