from tkinter import *
import time

import config
from gui import Gui
import moving
from detector import Detector

class GameMaker:
    def __init__(self):
        root = Tk()
        gui = Gui(root)
        ball = moving.Ball()
        paddleL = moving.PaddleL()
        paddleR = moving.PaddleR()
        items = {
            'ball': ball,
            'paddleL': paddleL,
            'paddleR': paddleR,
            }
        detector = Detector()
        self.game = Game(root, gui, items, detector)

    def __call__(self):
        return self.game


class Game:
    framelength = 1 / config.framerate

    def __init__(self, root, gui, items, detector):
        self.root = root
        self.gui = gui
        self.items = items
        for name, item in self.items.items():
            self.gui.addItem(name, item.getCoords())
        self.detector = detector
        self.registerEvents()
        
    def start(self):
        self.gameLoop()

    def checkCollisions(self):
        coords = [item.getCoords() for 
                  item in 
                  self.items.values()]
        self.detector.checkBounds(coords)

    def gameLoop(self):
        exit = False
        try:
            while not exit:
                start_time = time.clock()
                for name, item in self.items.items():
                    item.move()
                    self.checkCollisions()
                    #need to check for collision first
                    #then resolve collision
                    #then update gui.
                for name, item in self.items.items():
                    self.gui.move(name, item.getCoords())
                self.gui.process()
                #for item in self.items.values():
                interval = time.clock() - start_time
                pause = self.framelength - interval
                if pause > 0:
                    time.sleep(pause)
        except TclError:
            pass

    def registerEvents(self):
        self.root.bind('<Key>', self.keyEvent)
        self.root.bind('<KeyRelease>', self.keyUpEvent)

    def keyEvent(self, event):
        if event.keysym == 'Up':
            self.items['paddleR'].startUp()
        elif event.keysym == 'Down':
            self.items['paddleR'].startDown()
        elif event.keysym == 'Right':
            self.items['ball'].rotate()

    def keyUpEvent(self, event):
        if event.keysym == 'Up':
            self.items['paddleR'].stop()
        elif event.keysym == 'Down':
            self.items['paddleR'].stop()


