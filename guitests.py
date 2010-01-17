import unittest

from gui import Gui
import config
import moving

class GuiTests(unittest.TestCase):
    def setUp(self):
        self.gui = Gui()
        ball = moving.Ball()
        paddleL = moving.PaddleL()
        paddleR = moving.PaddleR()
        items = {
            'ball': ball,
            'paddleL': paddleL,
            'paddleR': paddleR,
            }
        for name, item in items.items():
            self.gui.addItem(name, item.coords)

    def testGuiHasBoard(self):
        self.gui.board

    def testBoardCorrectSize(self):
        self.assertEqual(int(self.gui.board.cget('width')),
                         config.BOARD_WIDTH)
        self.assertEqual(int(self.gui.board.cget('height')),
                         config.BOARD_HEIGHT)

    def testGuiHasItems(self):
        self.assertTrue('ball' in self.gui.items)
        self.assertTrue('paddleL' in self.gui.items)
        self.assertTrue('paddleR' in self.gui.items)

    
        
                        

    
        
    


class VisibleObjectTests(unittest.TestCase):
    def testFail(self):
        self.assertTrue(True)
        
