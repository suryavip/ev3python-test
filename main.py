#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color, SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

from threadedLogging import ThreadedLogging


def startStopSound(mode='start'):
    config = range(500, 1100, 100) if mode == 'start' else range(1000, 400, -100)
    for x in config:
        brick.sound.beep(x, 100)


class LogPowerUsage(ThreadedLogging):
    lastA = 0
    showPowerUsage = False

    def logPower(self):
        currentA = brick.battery.current()
        if currentA != self.lastA and self.showPowerUsage:
            print('Power usage: {} mA'.format(currentA))
        self.lastA = currentA

        currentV = brick.battery.voltage()
        if currentV < 7000:
            print('WARNING! Voltage supply drop below 7V ({} mV)'.format(currentV))
        if currentA > 500:
            print('WARNING! Power usage more than half amp ({} mA)'.format(currentA))

    def __init__(self, showPowerUsage=False):
        self.showPowerUsage = showPowerUsage
        ThreadedLogging(self.logPower)

# startStopSound()


powerLog = LogPowerUsage(showPowerUsage=True)

motorA = Motor(Port.A)
motorB = Motor(Port.B)
motorC = Motor(Port.C)

for speed in range(10, 101, 1):
    motorA.dc(speed)
    motorB.dc(speed)
    motorC.dc(speed)
    wait(100)

wait(1000)

motorA.stop()
motorB.stop()
motorC.stop()

powerLog.stop()

# startStopSound(mode='stop')
