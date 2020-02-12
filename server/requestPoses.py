#!/usr/bin/env python

import asyncio
import websockets
import json
import pyautogui
import ast

leftClickable = True
rightClickable = True
previousPosition = (0, 0)


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
        if not previousPosition[0] == int(data['x']) and not previousPosition[1] == int(data['y']):
            pyautogui.moveTo(1920 - (3 * float(data['x'])), 2.25 * float(data['y']))
            previousPosition = (int(data['x']), int(data['y']))

    def rightClick(self, wrist, nose):
        global rightClickable
        if wrist['y'] < nose['y'] and rightClickable:
            pyautogui.click(button='right')
            #print('Right Clicked')
            rightClickable = False
        elif wrist['y'] > nose['y'] and not rightClickable:
            rightClickable = True
            #print('Right Reset')

    def leftClick(self, wrist, nose):
        global leftClickable
        if wrist['y'] < nose['y'] and leftClickable:
            pyautogui.click(button='left')
            #print('Left Clicked')
            leftClickable = False
        elif wrist['y'] > nose['y'] and not leftClickable:
            leftClickable = True
            #print('Left Reset')

    def run(self):
        while True:
            try:
                event_loop = asyncio.new_event_loop()
                event_loop.run_until_complete(self.request())
            except:
                pass
