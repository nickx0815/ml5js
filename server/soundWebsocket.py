#!/usr/bin/env python
import asyncio
from server.data_singleton import soundData
import websockets

class receiveSoundWebsocket:

    async def receive(self, websocket, path):
        data = soundData.Instance()
        ps_data = await websocket.recv()
        data.set_data(ps_data)
        await websocket.send("OK")

    def run(self):
        new_loop = asyncio.new_event_loop()
        server = websockets.serve(self.receive, "localhost", 8010, loop=new_loop)
        new_loop.run_until_complete(server)
        new_loop.run_forever()

class transmitSoundWebsocket:

    async def transmit(self, websocket, path):
        data = soundData.Instance()
        get_ = await websocket.recv()
        data_ = data.get_data()
        await websocket.send(data_)

    def run(self):
        new_loop2 = asyncio.new_event_loop()
        server2 = websockets.serve(self.transmit, "localhost", 8090, loop=new_loop2)
        new_loop2.run_until_complete(server2)
        new_loop2.run_forever()
