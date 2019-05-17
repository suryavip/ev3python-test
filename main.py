#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

from threading import Thread
from time import sleep

def startStopSound(mode='start'):
    config = range(500, 1100, 100) if mode == 'start' else range(1000, 400, -100)
    for x in config:
        brick.sound.beep(x, 100)

class logPowerCurrentUsage():
    run = False
    lastValue = 0
    def log(self):
        while self.run:
            currentValue = brick.battery.current()
            if currentValue != self.lastValue:
                print('Power usage: {}mA'.format(currentValue))
            self.lastValue = currentValue
            sleep(0.1)
    def __init__(self):
        self.run = True
        t = Thread(target=self.log)
        t.start()
    def stop(self):
        self.run = False


startStopSound()

powerLog = logPowerCurrentUsage()

motorA = Motor(Port.A)
motorA.run_target(360 * 2, 360)
motorA.run_target(360 * 2, 0)

powerLog.stop()

startStopSound(mode='stop')