import sys
import unittest

import detector
import gui
import moving


                

class DetectorTests(unittest.TestCase):
    def setUp(self):
        """
        self.ball = Ball()
        self.paddleL = PaddleL()
        self.paddleR = PaddleR()
        self.items = {}
        self.items.update(ball=Ball(self.board))
        self.items.update(paddleL = PaddleL(self.board))
        self.items.update(paddleR = PaddleR(self.board))
        """
        
    def testBallCollidesWithWall(self):
        pass

    
def main():
    try:
        arg = sys.argv[1]
    except IndexError:
        arg = ''

    if arg == 'test':
        print('This is a test')
    else:
        game = gui.Gui()
        game.addItem('ball', moving.Ball())
        game.addItem('paddleL', moving.PaddleL())
        game.addItem('paddleR', moving.PaddleR())
        game.gameLoop()
        
    
        
if __name__ == '__main__':
    main()
