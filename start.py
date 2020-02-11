from threading import Thread
from server.asyncioWebsocket import receive_websocket
from server.asyncioWebsocket import transmit_websocket
from server.request import request_data
from server.seleniumWebsite import seleniumWebsite

def main():
    sw = seleniumWebsite()
    rw = receive_websocket()
    tw = transmit_websocket()
    rq = request_data()

    thread_selenium = Thread(target=sw.open)
    thread_recWebsocket = Thread(target=rw.run)
    thread_transWebsocket = Thread(target=tw.run)
    thread_request = Thread(target=rq.run)

    thread_selenium.start()
    thread_recWebsocket.start()
    thread_transWebsocket.start()
    thread_request.start()

if __name__ == '__main__':
    main()






