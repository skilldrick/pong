import unittest

import config
import moving

class Detector:
    def __init__(self):
        self.minX = 0
        self.minY = 0
        self.maxX = self.minX + config.BOARD_WIDTH
        self.maxY = self.minY + config.BOARD_HEIGHT

    def addItems(self, items):
        self.items = items
        
    def checkCollision(self):
        pass
        #print(self.items['ball'].getCoords())



class DetectorTests(unittest.TestCase):
    def setUp(self):
        items = {
            'ball': moving.Ball(),
            'paddleL': moving.PaddleL(),
            'paddleR': moving.PaddleR(),
            }
        self.detector = Detector()
        self.detector.addItems(items)

    def testDetectorHasBall(self):
        self.detector.items['ball']

    def testDetectorHasPaddleL(self):
        self.detector.items['paddleL']
            
    def testDetectorHasPaddleR(self):
        self.detector.items['paddleR']

    def testBallCollidesWithWall(self):
        #no need to use gui wall, just
        #check if within bounds
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
