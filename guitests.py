import unittest
from tkinter import *

from gui import Gui
import config
import moving

class GuiTests(unittest.TestCase):
    def setUp(self):
        self.root = Tk()
        self.gui = Gui(self.root)
        ball = moving.Ball()
        paddleL = moving.PaddleL()
        paddleR = moving.PaddleR()
        self.items = {
            'ball': ball,
            'paddleL': paddleL,
            'paddleR': paddleR,
            }
        for name, item in self.items.items():
            self.gui.addItem(name, item.getCoords())

    def testGuiHasBoard(self):
        self.gui.board

    def testBoardCorrectSize(self):
        self.assertEqual(int(self.gui.board.cget('width')),
                         config.BOARD_WIDTH)
        self.assertEqual(int(self.gui.board.cget('height')),
                         config.BOARD_HEIGHT)

    def testGuiHasItems(self):
        for name in self.items:
            self.assertTrue(name in self.gui.items)

    def testMoveMakesNewItem(self):
        testitem = 'testitem'
        self.gui.move(testitem, (20, 20, 30, 30))
        self.assertTrue(self.gui.items[testitem])

    def testMoveMoves(self):
        self.gui.move('ball',
                      self.items['ball'].getCoords())
        start = self.gui.items['ball'].coords
        self.items['ball'].move()
        self.gui.move('ball',
                      self.items['ball'].getCoords())
        end = self.gui.items['ball'].coords
        self.assertNotEqual(start, end)

    def testNoMove(self):
        self.gui.move('ball',
                      self.items['ball'].getCoords())
        start = self.gui.items['ball'].coords
        self.gui.move('ball',
                      self.items['ball'].getCoords())
        end = self.gui.items['ball'].coords
        self.assertEqual(start, end)
