from threading import Thread
from server.asyncioWebsocket import receive_websocket
from server.asyncioWebsocket import transmit_websocket

from server.request import request_data
#
from server.seleniumWebsite import seleniumWebsite

# sw = seleniumWebsite()
# sw.open()


tw = transmit_websocket()
t2 = Thread(target=tw.run)
t2.start()

rw = receive_websocket()
t = Thread(target=rw.run)
t.start()

rq = request_data()
t3 = Thread(target=rq.run)
t3.start()






