#!/usr/bin/env python

import asyncio
import websockets
import json
import pyautogui
import ast
from server.data_singleton import posesData

leftClickable = True
rightClickable = True
previousPosition = (0, 0)
resolution = (1920,1080)
p5Window = (640, 480)


class requestPoses:

    async def request(self):
        uri = "ws://localhost:8080"
        async with websockets.connect(uri) as websocket:
            await websocket.send("GET")
            _data = await websocket.recv()
            _data = ast.literal_eval(json.loads(_data))
            self.actions(_data)

    def actions(self, _data):
        if 'nose' in _data:
            self.mouseMove(_data['nose'])
        if 'rightWrist' in _data and 'nose' in _data:
            self.rightClick(_data['rightWrist'], _data['nose'])
        if 'leftWrist' in _data and 'nose' in _data:
            self.leftClick(_data['leftWrist'], _data['nose'])

    def mouseMove(self, data):
        global previousPosition
        global resolution
        global p5Window
        if not previousPosition[0] == int(data['x']) and not previousPosition[1] == int(data['y']):
            print("Move")
            #pyautogui.moveTo(int(resolution[0] - (resolution[0]/p5Window[0] * float(data['x']))), int(resolution[1]/p5Window[1] * float(data['y'])))
            previousPosition = (int(data['x']), int(data['y']))

    def rightClick(self, wrist, nose):
        global rightClickable
        if wrist['y'] < nose['y'] and rightClickable:
            print("Right")
            #pyautogui.click(button='right')
            rightClickable = False
        elif wrist['y'] > nose['y'] and not rightClickable:
            rightClickable = True
            print("Right Reset")

    def leftClick(self, wrist, nose):
        global leftClickable
        if wrist['y'] < nose['y'] and leftClickable:
            print("Left")
            #pyautogui.click(button='left')
            leftClickable = False
        elif wrist['y'] > nose['y'] and not leftClickable:
            leftClickable = True
            print("Left Reset")

    def run(self):
        while True:
            try:
                event_loop = asyncio.new_event_loop()
                event_loop.run_until_complete(self.request())
            except:
                pass
