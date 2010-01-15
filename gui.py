from tkinter import *
from tkinter import ttk
import time

#these two imports will be injected
import detector

BOARD_WIDTH = 100
BOARD_HEIGHT = 100

class Gui:
    framerate = 30
    framelength = 1 / framerate
    items = {}
    
    def __init__(self):
        self.root = Tk()
        self.gameFrame = ttk.Frame(self.root,
                              borderwidth=3,
                              relief='sunken')
        self.gameFrame.grid()
        self.scoreFrame = ttk.Frame(self.gameFrame,
                                    borderwidth=3,
                                    relief='sunken',
                                    width=BOARD_WIDTH,
                                    height=50)
        self.scoreFrame.grid()
        self.buildBoard()
        self.detector = detector.Detector(self.items)
        self.registerEvents()

    def addItem(self, itemName, item):
        newItem = {itemName:
                       VisibleObject(self.board, item)}
        self.items.update(newItem)

    def buildBoard(self):
        self.board = Canvas(self.gameFrame,
                            borderwidth=3,
                            relief='sunken',
                            width=BOARD_WIDTH,
                            height=BOARD_HEIGHT)
        self.board.grid()

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

    def gameLoop(self):
        try:
            exit = False
            while not exit:
                start_time = time.clock()
                for item in self.items.values():
                    item.move()
                for item in self.items.values():
                    pass #detect collisions
                self.root.update_idletasks()
                self.root.update()
                interval = time.clock() - start_time
                pause = self.framelength - interval
                if pause > 0:
                    time.sleep(pause)
        except TclError:
            pass


class VisibleObject:
    def __init__(self, board, item):
        self.movingObject = item
        self.coords = self.movingObject.getCoords()
        self.board = board
        self.id = self.board.create_rectangle(self.coords,
                                              fill='black')
    
        
    def move(self):
        self.movingObject.move()
        self.coords = self.movingObject.getCoords()
        self.board.coords(self.id, self.coords)

    def startUp(self):
        self.movingObject.startUp()
    
    def startDown(self):
        self.movingObject.startDown()

    def stop(self):
        self.movingObject.stop()

    
