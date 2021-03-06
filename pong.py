import sys
import optparse
import unittest

from game import GameMaker
import guitests
import movingtests
import detector

parser = optparse.OptionParser()
parser.add_option("-t", "--test", action="store_true")


    
def main():
    gameMaker = GameMaker()
    game = gameMaker()
    game.start()


def test():
    loader = unittest.TestLoader()
    detectorTests = loader.loadTestsFromTestCase(
        detector.DetectorTests)
    guiTests = loader.loadTestsFromTestCase(
        guitests.GuiTests)
    movingTests = loader.loadTestsFromTestCase(
        movingtests.MovingTests)

    allTests = unittest.TestSuite([detectorTests,
                                   guiTests,
                                   movingTests
                                   ])

    runner = unittest.TextTestRunner()
    result = runner.run(allTests)
    if not result.wasSuccessful():
        sys.exit(1)
    
        
    
        
if __name__ == '__main__':
    options, args = parser.parse_args()
    #this is needed for the unit tests to not get confused:
    del sys.argv[1:]
    if options.test:
        test()
    else:
        main()
