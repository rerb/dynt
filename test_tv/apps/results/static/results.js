var ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";
var ws_path = ws_scheme + '://' + window.location.host + '/dashboard/';
var socket = new WebSocket(ws_path);

socket.onopen = function(event) {
    socket.onmessage = function(event) {
        num_failures = event.data;
        var display = $("#numFailures");
        display.text(num_failures);
    };
    socket.onclose = function(event) {
    };
};
