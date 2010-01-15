import sys
import unittest
import optparse

import detector
import gui
import moving


parser = optparse.OptionParser()
parser.add_option("-t", "--test", action="store_true")


                

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
    game = gui.Gui()
    game.addItem('ball', moving.Ball())
    game.addItem('paddleL', moving.PaddleL())
    game.addItem('paddleR', moving.PaddleR())
    game.gameLoop()

def test():
    print('this is a test')
        
    
        
if __name__ == '__main__':
    options, args = parser.parse_args()
    if options.test:
        test()
    else:
        main()
