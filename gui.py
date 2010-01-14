from tkinter import *
from tkinter import ttk
import time
import math

import detector

BOARD_WIDTH = 100
BOARD_HEIGHT = 100

class Game:
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
        self.items.update(ball=Ball(self.board))
        self.items.update(paddleL = PaddleL(self.board))
        self.items.update(paddleR = PaddleR(self.board))
        self.detector = detector.Detector(self.items)
        self.registerEvents()

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
                self.items['ball'].calcVelocity()
                for item in self.items.values():
                    item.move()
                self.items['ball'].checkCollision()
                self.root.update_idletasks()
                self.root.update()
                interval = time.clock() - start_time
                pause = self.framelength - interval
                if pause > 0:
                    time.sleep(pause)
        except TclError:
            pass
            

class MovingObject:
    xvel = 0
    yvel = 0

    def startUp(self):
        self.yvel = -self.velocity

    def startDown(self):
        self.yvel = self.velocity

    def stop(self):
        self.xvel = 0
        self.yvel = 0
    
    def move(self):
        x1, y1, x2, y2 = self.board.coords(self.id)
        newcoords = (x1 + self.xvel,
                     y1 + self.yvel,
                     x2 + self.xvel,
                     y2 + self.yvel)
        self.board.coords(self.id, newcoords)

        
class Paddle(MovingObject):
    velocity = 2
    
    def __init__(self, board, originX):
        self.board = board
        width = 5
        height = 40
        originY = 50
        self.id = self.board.create_rectangle(
            (originX, originY,
             originX + width, originY + height),
            fill='black')
    

class PaddleL(Paddle):
    def __init__(self, board):
        Paddle.__init__(self, board, 10)

        
class PaddleR(Paddle):
    def __init__(self, board):
        Paddle.__init__(self, board, 90)

        
class Ball(MovingObject):
    velocity = 0.5
    angle = math.pi / 4
    
    def __init__(self, board):
        self.board = board
        width = 5
        height = 5
        originX = 40
        originY = 10
        self.id = self.board.create_rectangle(
            (originX, originY,
             originX + width, originY + height),
            fill='black')

    def calcVelocity(self):
        adj = math.cos(self.angle) * self.velocity
        opp = math.sin(self.angle) * self.velocity
        self.xvel = adj
        self.yvel = opp

    def stop(self):
        self.velocity = 0
        
    def rotate(self):
        self.angle += math.pi / 4

    def checkCollision(self):
        x1, y1, x2, y2 = self.board.coords(self.id)
        if x2 > 80 or y2 > 80:
            self.stop()
