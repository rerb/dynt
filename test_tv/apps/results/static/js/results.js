function openSocket(path, onMessage) {
    var wsScheme = window.location.protocol == "https:" ? "wss" : "ws";
    var wsPath = wsScheme + '://' + window.location.host + path;
    var socket = new WebSocket(wsPath);

    socket.onopen = function(event) {
        socket.onmessage = function(event) {
            onMessage();
        };
        socket.onclose = function(event) {
        };
    };

    return socket;
};

function connectSocketToElement(path, elementId) {
    openSocket(path, function() {
        var targetElement = document.getElementById(elementId);
        targetElement.innerHTML = event.data;
    });
};

connectSocketToElement("/num-failures", "numFailures");
connectSocketToElement("/num-errors", "numErrors");
connectSocketToElement("/num-successes", "numSuccesses");
connectSocketToElement("/num-left", "numLeft");
