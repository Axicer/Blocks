from threading import Thread
import pygame
import time

pygame.font.init()


class Timer(Thread):

    def __init__(self, min: int, sec: int, posX: int, posY: int, window):
        Thread.__init__(self)
        self.min = min
        self.sec = sec
        self.posX = posX
        self.posY = posY
        self.started = True
        self.show = True
        self.window = window
        self.font = pygame.font.SysFont('Comic Sans MS', 30)

    def stop(self):
        self.started = False

    def run(self):
        while self.started:
            time.sleep(1)
            self.sec -= 1
            if self.sec < 0:
                self.min -= 1
                self.sec = 59
            if self.min == 0 and self.sec == 0:
                self.stop()

    def getMinutes(self):
        return self.min

    def getSeconds(self):
        return self.sec
