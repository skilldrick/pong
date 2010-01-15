import unittest


class Detector:
    def __init__(self):
        pass

    def addItems(self, items):
        self.items = items
        
    def checkCollision(self):
        pass



class DetectorTests(unittest.TestCase):
    def testBallCollidesWithWall(self):
        self.failIf(True)





if __name__ == '__main__':
    unittest.main()
