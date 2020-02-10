#!/usr/bin/env python

# WS client example

import asyncio
import websockets
import json
import pyautogui
import ast

leftClickable = True
rightClickable = True

class request_data:

    async def request(self):
        print("jo")
        uri = "ws://localhost:8080"
        async with websockets.connect(uri) as websocket:
            await websocket.send("GET")
            _data = await websocket.recv()
            _data = ast.literal_eval(json.loads(_data))
            if 'nose' in _data:
                self.mouseMove(_data['nose'])
            if 'rightWrist' in _data:
                self.rightClick(_data['rightWrist'], _data['rightShoulder'])
            if 'leftWrist' in _data:
                self.leftClick(_data['leftWrist'], _data['leftShoulder'])


    def mouseMove(self,data):
        pyautogui.moveTo(1920 - (3 * float(data['x'])), 2.25 * float(data['y']))


    def rightClick(self,dataWrist, dataShoulder):
        global rightClickable
        if float(dataWrist['y']) < float(dataShoulder['y']) and rightClickable:
            #pyautogui.click(button='right')
            print('Right Clicked')
            rightClickable = False
        if float(dataWrist['y']) > float(dataShoulder['y']) and not rightClickable:
            rightClickable = True
            print('Right Reset')


    def leftClick(self,dataWrist, dataShoulder):
        global leftClickable
        if float(dataWrist['y']) < float(dataShoulder['y']) and leftClickable:
            #pyautogui.click(button='right')
            print('Left Clicked')
            leftClickable = False
        if float(dataWrist['y']) > float(dataShoulder['y']) and not leftClickable:
            leftClickable = True
            print('Left Reset')

    def run(self):
        while True:
            try:
                asyncio.get_event_loop().run_until_complete(self.request())
                print('He')
            except:
                pass

rq = request_data()
rq.run()