import asyncio
from server import data_singleton
import websockets
from server.seleniumWebsite import seleniumWebsite



data = ""
r_count = 0
t_count = 0

class receive_websocket:

    async def receive(self, websocket, path):
        # global r_count
        # r_count += 1
        # print("received: "+str(r_count))
        #global data
        data = data_singleton.data_store.Instance()
        ps_data = await websocket.recv()
        data.set_data(ps_data)
        await websocket.send("OK")

    def run(self):
        new_loop = asyncio.new_event_loop()
        server = websockets.serve(self.receive, "localhost", 8000, loop=new_loop)
        new_loop.run_until_complete(server)
        new_loop.run_forever()

class transmit_websocket:

    async def transmit(self, websocket, path):
        #global data
        # global t_count
        # t_count += 1
        # print("transmitted: "+str(t_count))
        data = data_singleton.data_store.Instance()
        get_ = await websocket.recv()
        data_ = data.get_data()
        await websocket.send(data_)

    def run(self):
        new_loop2 = asyncio.new_event_loop()
        server2 = websockets.serve(self.transmit, "localhost", 8080, loop=new_loop2)
        new_loop2.run_until_complete(server2)
        new_loop2.run_forever()





