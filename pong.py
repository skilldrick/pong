from tkinter import *
from tkinter import ttk
import time

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

        self.registerEvents()

        #self.root.update()
        self.gameLoop()

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

    def keyUpEvent(self, event):
        self.items['paddleR'].stop()
        if event.keysym == 'Up':
            pass
            #self.items['paddleR'].stop()
        elif event.keysym == 'Down':
            pass
            #self.items['paddleR'].stop()
            

    def gameLoop(self):
        try:
            exit = False
            while not exit:
                start_time = time.clock()
                for item in self.items.values():
                    item.update()
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
        self.yvel = -1

    def startDown(self):
        self.yvel = 1

    def stop(self):
        self.xvel = 0
        self.yvel = 0
    
    def update(self):
        self.move(self.xvel, self.yvel)
    
    def move(self, x, y):
        x1, y1, x2, y2 = self.board.coords(self.id)
        x1 += x
        x2 += x
        y1 += y
        y2 += y
        self.board.coords(self.id, (x1, y1, x2, y2))

        
class Paddle(MovingObject):
    def __init__(self, board, originX):
        self.board = board
        width = 5
        height = 40
        originY = 50
        self.id = self.board.create_rectangle(
            (originX, originY,
             originX + width, originY + height),
            fill='black')

    def moveUp(self):
        self.move(0, -1)

    def moveDown(self):
        self.move(0, 1)
    

class PaddleL(Paddle):
    def __init__(self, board):
        Paddle.__init__(self, board, 10)

class PaddleR(Paddle):
    def __init__(self, board):
        Paddle.__init__(self, board, 90)

class Ball(MovingObject):
    def __init__(self, board):
        self.board = board
        width = 5
        height = 5
        originX = 40
        originY = 40
        self.id = self.board.create_rectangle(
            (originX, originY,
             originX + width, originY + height),
            fill='black')

        



def main():
    game = Game()
    
        
if __name__ == '__main__':
    main()
