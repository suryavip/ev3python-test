from threading import Thread
from time import sleep


class ThreadedLogging():
    run = False
    rate = 100

    def log(self):
        while self.run:
            self.logMethod()
            sleep(self.rate / 1000)

    def __init__(self, logMethod, rate=100):
        self.run = True
        self.logMethod = logMethod
        self.rate = rate
        t = Thread(target=self.log)
        t.start()

    def stop(self):
        self.run = False
