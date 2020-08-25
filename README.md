# `cubing.py`

## Websocket Proxy

Install [`mkcert`](https://github.com/FiloSottile/mkcert). This is needed for testing using HTTPS so that real websites can connect to the Python server.

Then run:

    make

This will prompt you to install a certificate (probably using your password for permission).

Then visit https://twizzle.net/?go=keyboard&socketOrigin=wss://python.localhost:8765 to display the events from the proxy.

You can then broadcast events from Python. Optionally, you can also connect a sender at https://experiments.cubing.net/cubing.js/vr/proxy/proxy.html?socketOrigin=wss://python.localhost:8765 to send data to the proxy from Bluetooth or keyboard input.

The code sends a test event 2 seconds after a new receiver connects. Change `SEND_TEST_EVENT` to `False` to remove this behaviour.
