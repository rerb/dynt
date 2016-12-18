# Test TV Django Test Runner

1. Starts `test_tv` server to serve `results` application.

2. Runs tests.

3. Records results (including STDOUT, STDERR (inc. tracebacks)) in
   database.

4. When tests are done, waits 5s (for clients to make final queries)
   then stops `test_tv` server.
   
# Test TV Server

The Django project called `test_tv`.  Serves a Django app called `results`.

Serves the app via `runserver` since it's sufficient and allows us to use 
the simplest ASGI channel layer, in-memory.

## API

* `/dashboard` - main page (html) contains links to channels below
* `/num_failures` (int channel)
* `/num_successes` (int channel)
* `/num_errors` (int channel)
* `/num_left` (int channel)
* `/failures` (json channel (name:"", stdout:"", stderr=""))
* `/errors` (json channel (name:"", stdout:"", stderr=""))

# `results`, the Django app served by `test_tv` server.

Defines models Test and TestResult.

TestResult exposes an API for quering test results.

Currently only supports summary totals for numbers of failures, errors,
successes, and tests left to run.  Support for JSON objects like STDERR,
exceptions, tracebacks, etc., is planned.

# `results.js`, the browser-hosted Javascript app

Receives data from the Django `results` app and updates the browser's
DOM appropriately.

Associates a simple web socket for each data point (e.g., number of
failures, number of errors, tracebacks, etc.) to the corresponding
HTML element in dashboard.html.

Each socket pings host every 1s.  That's the current implementation,
though the plan is to replace this polling with messages pushed to 
the client triggered by database updates/object saves.
