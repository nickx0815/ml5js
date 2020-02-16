from threading import Thread
from server.posesWebsocket import receivePosesWebsocket
from server.posesWebsocket import transmitPosesWebsocket
from server.soundWebsocket import receiveSoundWebsocket
from server.soundWebsocket import transmitSoundWebsocket
from control.requestPoses import requestPoses
from control.requestSound import requestSound
from control.seleniumWebsite import seleniumWebsite

def main():
    sw = seleniumWebsite()
    rp = receivePosesWebsocket()
    tp = transmitPosesWebsocket()
    rs = receiveSoundWebsocket()
    ts = transmitSoundWebsocket()

    rposes = requestPoses()
    rsound = requestSound()

    webdriverBrowser, webdriverPosenet = sw.open()
    thread_recPoses = Thread(target=rp.run)
    thread_transPoses = Thread(target=tp.run)

    thread_recSound = Thread(target=rs.run)
    thread_transSound = Thread(target=ts.run)

    thread_requestPoses = Thread(target=rposes.run)
    thread_requestSound = Thread(target=rsound.run, args=(webdriverBrowser,webdriverPosenet,))

    thread_recPoses.start()
    thread_transPoses.start()
    thread_recSound.start()
    thread_transSound.start()
    thread_requestPoses.start()
    thread_requestSound.start()

if __name__ == '__main__':
    main()






