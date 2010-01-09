from tkinter import *
from tkinter import ttk

BOARD_WIDTH = 100
BOARD_HEIGHT = 100

class Board:
    def __init__(self, parent):
        self.canvas = Canvas(parent,
                             width=BOARD_WIDTH,
                             height=BOARD_HEIGHT)
        self.canvas.grid()
        self.ball = Ball(self)



class Paddle:
    def __init__(self):
        pass


class Ball:
    def __init__(self, board):
        self.board = board
        self.ball = self.board.canvas.create_rectangle((10, 10, 20, 20),
                                                       fill='black')

    def moveUp(self):
        self.board.canvas.coords(self.ball, (10, 11, 12, 13))
        



def main():
    root = Tk()

    scoreFrame = ttk.Frame(root,
                           borderwidth=3,
                           relief='sunken',
                           width=BOARD_WIDTH, height=50)
    scoreFrame.grid()

    gameFrame = ttk.Frame(root,
                          borderwidth=3,
                          relief='sunken')
    gameFrame.grid()



    board = Board(gameFrame)

    def registerEvents(root):
        root.bind('<Key>', move)

    def move(event):
        if event.keysym == 'Up':
            board.ball.moveUp()
        elif event.keysym == 'Down':
            print('Down')
        
    registerEvents(root)
    root.mainloop()

    
    
        
if __name__ == '__main__':
    main()
