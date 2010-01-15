import sys
import optparse
import unittest

import detector
import gui
import moving


parser = optparse.OptionParser()
parser.add_option("-t", "--test", action="store_true")


    
def main():
    game = gui.Gui()
    game.addItem('ball', moving.Ball())
    game.addItem('paddleL', moving.PaddleL())
    game.addItem('paddleR', moving.PaddleR())
    game.addDetector(detector.Detector())
    game.gameLoop()



def test():
    detectorTests = detector.DetectorTests
    suite = unittest.makeSuite(detectorTests, 'test')

    runner = unittest.TextTestRunner()
    runner.run(suite)
    
        
if __name__ == '__main__':
    options, args = parser.parse_args()
    del sys.argv[1:]
    if options.test:
        test()
    else:
        main()
