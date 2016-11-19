# Test TV Django Test Runner

1. Starts `test_tv` server to serve `results` application.

2. Runs tests.

3. Feeds results (including STDOUT, STDERR (inc. tracebacks)) to
   `test-tv.js` application (simple Javascript) running in web
   browser, as they become available.

4. When tests are done, pushes final results to `test-tv.js`
   application in browser, then stops `test_tv` server.

# Test TV Server

The Django project called `test_tv`.  Serves a Django app called `results`.

## API

* `/dashboard` - main page (html) contains links to channels below
* `/num_failures` (int channel)
* `/num_successes` (int channel)
* `/num_errors` (int channel)
* `/tests_left` (int channel)
* `/failures` (json channel (name:"", stdout:"", stderr=""))
* `/errors` (json channel (name:"", stdout:"", stderr=""))

# `results`, the Django app served by `test_tv` server.

* Implementation

# `results.js`, the browser-hosted Javascript app

Receives data from the Django `results` app and updates the browser's DOM appropriately.

* Implementation

** Creates simple web socket.

** Sets up a listener to load the number of test failures each time it
   receives a message. Number of test failures loads when "socket
   open" message is received.
