#!/usr/bin/env python

# WS client example

import asyncio
import websockets
import json
import pyautogui
import ast

leftClickable = True
rightClickable = True


async def request():
    uri = "ws://localhost:8080"
    async with websockets.connect(uri) as websocket:
        await websocket.send("GET")
        _data = await websocket.recv()
        _data = ast.literal_eval(json.loads(_data))
        if 'nose' in _data:
            mouseMove(_data['nose'])
        if 'rightWrist' in _data:
            rightClick(_data['rightWrist'], _data['rightShoulder'])
        if 'leftWrist' in _data:
            leftClick(_data['leftWrist'], _data['leftShoulder'])


def mouseMove(data):
    pyautogui.moveTo(1920 - (3 * float(data['x'])), 2.25 * float(data['y']))


def rightClick(dataWrist, dataShoulder):
    global rightClickable
    if float(dataWrist['y']) < float(dataShoulder['y']) and rightClickable:
        #pyautogui.click(button='right')
        print('Right Clicked')
        rightClickable = False
    if float(dataWrist['y']) > float(dataShoulder['y']) and not rightClickable:
        rightClickable = True
        print('Right Reset')


def leftClick(dataWrist, dataShoulder):
    global leftClickable
    if float(dataWrist['y']) < float(dataShoulder['y']) and leftClickable:
        #pyautogui.click(button='right')
        print('Left Clicked')
        leftClickable = False
    if float(dataWrist['y']) > float(dataShoulder['y']) and not leftClickable:
        leftClickable = True
        print('Left Reset')


for x in range(0, 50):
    try:
        asyncio.get_event_loop().run_until_complete(request())
    except:
        pass
