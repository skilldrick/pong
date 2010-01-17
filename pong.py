import sys
import optparse
import unittest

from game import GameMaker
import guitests
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
    visibleObjectTests = loader.loadTestsFromTestCase(
        guitests.VisibleObjectTests)

    allTests = unittest.TestSuite([detectorTests,
                                   guiTests,
                                   visibleObjectTests])

    runner = unittest.TextTestRunner()
    runner.run(allTests)
    
        
if __name__ == '__main__':
    options, args = parser.parse_args()
    del sys.argv[1:]
    if options.test:
        test()
    else:
        main()
