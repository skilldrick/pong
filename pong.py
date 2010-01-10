from tkinter import *
from tkinter import ttk
import time

BOARD_WIDTH = 100
BOARD_HEIGHT = 100

class Game:
    framerate = 30
    framelength = 1 / framerate
    
    def __init__(self):
        self.root = Tk()
        self.scoreFrame = ttk.Frame(self.root,
                                    borderwidth=3,
                                    relief='sunken',
                                    width=BOARD_WIDTH, height=50)
        self.scoreFrame.grid()

        self.gameFrame = ttk.Frame(self.root,
                              borderwidth=3,
                              relief='sunken')
        self.gameFrame.grid()

        self.board = Board(self.gameFrame)

        self.registerEvents()

        #self.root.mainloop()
        self.root.update()
        self.gameLoop()

    def registerEvents(self):
        self.root.bind('<Key>', self.keyEvent)

    def keyEvent(self, event):
        if event.keysym == 'Up':
            self.board.ball.moveUp()
        elif event.keysym == 'Down':
            self.board.ball.moveDown()

    def gameLoop(self):
        try:
            exit = False
            while not exit:
                start_time = time.clock()
                
                self.root.update_idletasks()
                self.root.update()
                interval = time.clock() - start_time
                pause = self.framelength - interval
                if pause > 0:
                    time.sleep(pause)
        except TclError:
            pass
            
            



class Board:
    def __init__(self, parent):
        self.canvas = Canvas(parent,
                             width=BOARD_WIDTH,
                             height=BOARD_HEIGHT)
        self.canvas.grid()
        self.ball = Ball(self.canvas)



class Paddle:
    def __init__(self):
        pass


class Ball:
    def __init__(self, canvas):
        self.canvas = canvas
        self.id = self.canvas.create_rectangle((10, 10, 20, 20),
                                                 fill='black')

    def moveUp(self):
        self.move(-1)

    def moveDown(self):
        self.move(1)
        
    def move(self, amount):
        x1, y1, x2, y2 = self.canvas.coords(self.id)
        y1 += amount
        y2 += amount
        self.canvas.coords(self.id, (x1, y1, x2, y2))



def main():
    game = Game()
    
        
if __name__ == '__main__':
    main()
