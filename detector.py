import unittest

import config
import moving


class Detector:
    def __init__(self):
        minX = 0
        minY = 0
        maxX = minX + config.BOARD_WIDTH
        maxY = minY + config.BOARD_HEIGHT
        self.bounds = (minX, minY, maxX, maxY)

    def checkCollision(self, coordsA, coordsB):
        if coordsA[0] >= coordsB[2]:
            return False
        if coordsA[2] <= coordsB[0]:
            return False
        if coordsA[1] >= coordsB[3]:
            return False
        if coordsA[3] <= coordsB[1]:
            return False
        return True

    def checkBounds(self, coords):
        results = []
        for coord in coords:
            if coord[0] < self.bounds[0]:
                results.append('left')
            elif coord[1] < self.bounds[1]:
                results.append('top')
            elif coord[2] > self.bounds[2]:
                results.append('right')
            elif coord[3] > self.bounds[3]:
                results.append('bottom')
            else:
                results.append(False)
        return results
            

class DetectorTests(unittest.TestCase):
    def setUp(self):
        self.minX = 0
        self.minY = 0
        self.maxX = self.minX + config.BOARD_WIDTH
        self.maxY = self.minY + config.BOARD_HEIGHT
        
        self.detector = Detector()

    def testBallDoesntCollideWithWall(self):
        inCoords = (
            (0, 0, 10, 10),
            (self.maxX - 10, self.maxY - 10,
             self.maxX, self.maxY),
            (self.maxX - 10, 0, self.maxX, 10),
            (0, self.maxY - 10, 10, self.maxY))
        results = self.detector.checkBounds(inCoords)
        for result in results:
            self.assertFalse(result)
    
    def testBallCollidesWithWall(self):
        outCoords = (
            (-1, 20, 9, 30),
            (40, -1, 50, 9),
            (-1000, -1000, -990, -990),
            (1000, 1000, 1010, 1010),
            (self.maxX - 9, self.maxY - 9,
             self.maxX + 1, self.maxY + 1)
            )
        results = self.detector.checkBounds(outCoords)
        for result in results:
            self.assertTrue(result)

    def testObjectsCollide(self):
        object1 = (10, 10, 20, 20)
        object2 = (19, 19, 29, 29)
        self.assertTrue(self.detector.checkCollision(object1, object2))

    def testObjectsDontCollide(self):
        object1 = (10, 10, 20, 20)
        object2 = (21, 10, 31, 20)
        self.assertFalse(self.detector.checkCollision(object1, object2))


if __name__ == '__main__':
    unittest.main()
