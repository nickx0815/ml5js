import time
from http.server import HTTPServer
from server import Server
import threading
from threading import Thread
import requests
import pyautogui

class webserver(Thread):
    HOST_NAME = 'localhost'
    PORT_NUMBER = 8000

    def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter
    
    def run(self):
      self.start_server()
    
    def start_server(self):
        httpd = HTTPServer((self.HOST_NAME, self.PORT_NUMBER), Server)
        print(time.asctime(), 'Server UP - %s:%s' % (self.HOST_NAME, self.PORT_NUMBER))
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            pass
        httpd.server_close()
        print(time.asctime(), 'Server DOWN - %s:%s' % (self.HOST_NAME, self.PORT_NUMBER))

    # if __name__ == '__main__':
    #     httpd = HTTPServer((HOST_NAME, PORT_NUMBER), Server)
    #     print(time.asctime(), 'Server UP - %s:%s' % (HOST_NAME, PORT_NUMBER))
    #     try:
    #         httpd.serve_forever()
    #     except KeyboardInterrupt:
    #         pass
    #     httpd.server_close()
    #     print(time.asctime(), 'Server DOWN - %s:%s' % (HOST_NAME, PORT_NUMBER))

class mouse_request(Thread):

    def __init__(self, threadID, name, counter):
        pyautogui.FAILSAFE = False
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    
    def run(self):
        while True:
            self.req()

    def req(self):
        try:
            req = requests.get('http://localhost:8000/mouse/', timeout=0.5)
            req_cont = req.content.split()
            #print(3*int(req_cont[0]), 1080-(2.125*int(req_cont[1]) ))
            pyautogui.moveTo(1920 - (3*int(req_cont[0])), 2.125*int(req_cont[1]) )
            #pyautogui.moveTo(100,100)
            req.close()
        except KeyboardInterrupt:
            pass

thread1 = webserver(1, 'thread1', 1)
thread2 = mouse_request(2, 'thread2', 2)
try:
    thread1.start()
    thread2.start()
except KeyboardInterrupt:
    pass
thread1.join()
thread2.join()


# try:
#     # while True:
    
#         req()
# except KeyboardInterrupt:
#     raise TypeError("Request Stopped")