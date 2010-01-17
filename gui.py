from tkinter import *
from tkinter import ttk


import config


class Gui:
    items = {}
    
    def __init__(self, root):
        self.root = root
        self.gameFrame = ttk.Frame(self.root,
                              borderwidth=3,
                              relief='sunken')
        self.gameFrame.grid()
        self.scoreFrame = ttk.Frame(self.gameFrame,
                                    borderwidth=3,
                                    relief='sunken',
                                    width=config.BOARD_WIDTH + 6,
                                    height=50)
        self.scoreFrame.grid()
        self.buildBoard()

    def addItem(self, name, coords):
        newItem = {name: VisibleObject(self.board, coords)}
        self.items.update(newItem)

    def buildBoard(self):
        self.board = Canvas(self.gameFrame,
                            borderwidth=3,
                            relief='sunken',
                            width=config.BOARD_WIDTH,
                            height=config.BOARD_HEIGHT)
        self.board.grid()

    def move(self, name, coords):
        try:
            self.items[name].move(coords)
        except KeyError:
            self.addItem(name, coords)
    
    def process(self):
        self.root.update_idletasks()
        self.root.update()


class VisibleObject:
    def __init__(self, board, coords, colour='black'):
        self.coords = coords
        self.board = board
        self.id = self.board.create_rectangle(self.coords,
                                              fill=colour)

    def move(self, coords):
        self.coords = coords
        self.board.coords(self.id, self.coords)
