from tkinter import *
import time

import config
from gui import Gui
import moving
from detector import Detector

class GameMaker:
    def __init__(self):
        gui = Gui()
        ball = moving.Ball()
        paddleL = moving.PaddleL()
        paddleR = moving.PaddleR()
        items = {
            'ball': ball,
            'paddleL': paddleL,
            'paddleR': paddleR,
            }
        detector = Detector()
        self.game = Game(gui, items, detector)

    def __call__(self):
        return self.game


class Game:
    framelength = 1 / config.framerate

    def __init__(self, gui, items, detector):
        self.gui = gui
        self.items = items
        for name, item in self.items.items():
            self.gui.addItem(name, item.coords)
        self.detector = detector
        
    def start(self):
        self.gameLoop()

    def gameLoop(self):
        exit = False
        try:
            while not exit:
                start_time = time.clock()
                for name, item in self.items.items():
                    item.move()
                    #need to check for collision first
                    #then resolve collision
                    #then update gui.
                for name, item in self.items.items():
                    self.gui.move(name, item.coords)
                self.gui.process()
                #for item in self.items.values():
                interval = time.clock() - start_time
                pause = self.framelength - interval
                if pause > 0:
                    time.sleep(pause)
        except TclError:
            pass

