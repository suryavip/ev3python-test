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


powerLog = LogPowerUsage(showPowerUsage=False)

brick.sound.file(SoundFile.HELLO)
while Button.CENTER not in brick.buttons():
    if Button.LEFT in brick.buttons():
        brick.sound.file(SoundFile.LEFT)
    elif Button.RIGHT in brick.buttons():
        brick.sound.file(SoundFile.RIGHT)
    elif Button.UP in brick.buttons():
        brick.sound.file(SoundFile.UP)
    elif Button.DOWN in brick.buttons():
        brick.sound.file(SoundFile.DOWN)
    wait(10)
brick.sound.file(SoundFile.GOODBYE)

'''motorA = Motor(Port.A)

#motorB = Motor(Port.B)
#motorC = Motor(Port.C)

for speed in range(20, 101, 1):
    motorA.dc(speed)
    #motorB.dc(speed)
    #motorC.dc(speed)
    wait(10)

wait(2000)

motorA.stop()
#motorB.stop()
#motorC.stop()'''

powerLog.stop()

# startStopSound(mode='stop')
