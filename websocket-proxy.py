#!/usr/bin/env python

# Adapted from https://websockets.readthedocs.io/en/stable/intro.html

import asyncio
import json
import logging
import websockets
import ssl

logging.basicConfig()

SENDERS = set()
RECEIVERS = set()

SEND_TEST_EVENT = True


async def broadcast(message):
    if RECEIVERS:  # asyncio.wait doesn't accept an empty list
        print(f"Broadcasting: {message}")
        await asyncio.wait([user.send(message) for user in RECEIVERS])


# This will broadcast all three possible events.
async def testSend(delaySeconds):
    await asyncio.sleep(delaySeconds)
    await broadcast(json.dumps({
        "event": "reset"
    }))
    await broadcast(json.dumps({
        "event": "orientation",
        "data": {
            "quaternion": {
                    "x":  0.2917,
                    "y": -0.0668,
                    "z":  0.1929,
                    "w":  0.9332
                    },
            "timeStamp": 35055.8
        }
    }))
    await broadcast(json.dumps({
        "event": "move",
        "data": {
            "latestMove": {
                    "family": "R",
                    "amount": 1,
                    "type": "blockMove"
                    },
            "timeStamp": 3328.1950000018696,
        }
    }))


async def serve(websocket, path):
    if path == "/register-receiver":
        RECEIVERS.add(websocket)
        print("Receiver added!")
        try:
            if SEND_TEST_EVENT:
                await testSend(2)
            async for message in websocket:
                await print("A receiver sent a message. Ignoring.")
        finally:
            RECEIVERS.remove(websocket)
            print("Receiver removed!")
    elif path == "/register-sender":
        SENDERS.add(websocket)
        print("Sender added!")
        try:
            async for message in websocket:
                print(f"Received message!")
                await broadcast(message)
        finally:
            SENDERS.remove(websocket)
            print("Sender removed!")


ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ssl_context.load_cert_chain("./python.localhost-key.pem")

start_server = websockets.serve(
    serve, "python.localhost", 8765, ssl=ssl_context,
    extra_headers=[("Access-Control-Alllow-Origin", "*")]
)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
