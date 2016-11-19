from channels.routing import route


channel_routing = [
    route('websocket.connect',
          'test_tv.apps.results.consumers.ws_connect'),
    route('websocket.receive',
          'test_tv.apps.results.consumers.ws_receive'),
    route('test_tv.results.num_failures',
          'test_tv.apps.results.consumers.num_failures')
]
