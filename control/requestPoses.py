#!/usr/bin/env python

import asyncio
import websockets
import json
import pyautogui
import ast
from server.data_singleton import posesData


class requestPoses:

    def __init__(self):
        self.leftClickable = True
        self.rightClickable = True
        self.previousPosition = (0, 0)
        self.resolution = (1920, 1080)
        self.p5Window = (640, 480)

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
        if not self.previousPosition[0] == int(data['x']) and not self.previousPosition[1] == int(data['y']):
            pyautogui.moveTo(int(self.resolution[0] - (self.resolution[0] / self.p5Window[0] * float(data['x']))),
                             int(self.resolution[1] / self.p5Window[1] * float(data['y'])))
            self.previousPosition = (int(data['x']), int(data['y']))

    def rightClick(self, wrist, nose):
        if wrist['y'] < nose['y'] and self.rightClickable:
            pyautogui.click(button='right')
            self.rightClickable = False
        elif wrist['y'] > nose['y'] and not self.rightClickable:
            self.rightClickable = True

    def leftClick(self, wrist, nose):
        if wrist['y'] < nose['y'] and self.leftClickable:
            pyautogui.click(button='left')
            self.leftClickable = False
        elif wrist['y'] > nose['y'] and not self.leftClickable:
            self.leftClickable = True

    def run(self):
        pData = posesData.Instance()
        while True:
            status = pData.get_status()
            if status:
                try:
                    event_loop = asyncio.new_event_loop()
                    event_loop.run_until_complete(self.request())
                except:
                    pass

