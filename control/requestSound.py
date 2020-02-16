#!/usr/bin/env python

import asyncio
import websockets
import json
import ast
import pyautogui


class requestSound:

    def __init__(self):
        self.domainList = {'google': 'https://www.google.de/?gws_rd=ssl',
                           'youtube': 'https://www.youtube.com/?gl=DE',
                           'host': 'https://www.hochschule-stralsund.de/',
                           'amazon': 'https://www.amazon.de/',
                           'paypal': 'https://www.paypal.com/de/home',
                           'netflix': 'https://www.netflix.com/de/Login?nextpage=https%3A%2F%2Fwww.netflix.com%2Fbrowse'}

        self.actionList = ['back', 'forward', 'close', 'rightClick', 'leftClick']

    async def request(self, webdriverBrowser, webdriverPosenet):
        uri = "ws://localhost:8090"
        async with websockets.connect(uri) as websocket:
            await websocket.send("GET")
            _data = await websocket.recv()
            _data = ast.literal_eval(json.loads(_data))
            self.actions(_data, webdriverBrowser, webdriverPosenet)

    def actions(self, _data, webdriverBrowser, webdriverPosenet):
        if _data[0]['label'] in self.actionList and _data[0]['confidence'] > 0.9:
            if _data[0]['label'] == "back":
                webdriverBrowser.back()
            elif _data[0]['label'] == "forward":
                webdriverBrowser.forward()
            elif _data[0]['label'] == "close":
                webdriverBrowser.close()
                webdriverPosenet.close()
            elif _data[0]['label'] == "rightClick":
                pyautogui.click(button='right')
            elif _data[0]['label'] == "leftClick":
                pyautogui.click(button='left')
        elif not _data[0]['label'] in webdriverBrowser.current_url and _data[0]['label'] in self.domainList and \
                _data[0]['confidence'] > 0.8:
            webdriverBrowser.get(self.domainList[_data[0]['label']])

    def run(self, webdriverBrowser, webdriverPosenet):
        while True:
            try:
                event_loop = asyncio.new_event_loop()
                event_loop.run_until_complete(self.request(webdriverBrowser, webdriverPosenet))
            except:
                pass
