import requests
import pyautogui

class mouse_request():

    def req():
        try:
            req = requests.get('http://localhost:8000/mouse/', timeout=0.5)
            req_cont = req.content.split()
            #print(3*int(req_cont[0]), 1080-(2.125*int(req_cont[1]) ))
            pyautogui.moveTo(1920 - (3*int(req_cont[0])), 2.125*int(req_cont[1]) )
            #pyautogui.moveTo(100,100)
            req.close()
        except:
            return


try:
    # while True:
    for x in range(0,50):
        req()
except KeyboardInterrupt:
    raise TypeError("Request Stopped")