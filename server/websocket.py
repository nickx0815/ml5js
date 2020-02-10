import asyncio
from server import data_singleton
import websockets

data = ""

#class websocket():
async def receive(websocket, path):
    global data
    data = data_singleton.data_store.Instance()
    ps_data = await websocket.recv()
    data.set_data(ps_data)
    await websocket.send("OK")


async def transmit(websocket, path):
    global data
    data = data_singleton.data_store.Instance()
    get_ = await websocket.recv()
    data_ = data.get_data()
    await websocket.send(data_)




    #def run(self):
try:
    start_server_receive = websockets.serve(receive, "localhost", 8000)
    start_server_transmit = websockets.serve(transmit, "localhost", 8080)
except:
    pass
asyncio.get_event_loop().run_until_complete(start_server_receive)
asyncio.get_event_loop().run_until_complete(start_server_transmit)
asyncio.get_event_loop().run_forever()
        #return 'test'
