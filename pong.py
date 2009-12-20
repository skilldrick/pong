import unittest
import Tkinter

class MainWindow:
    def makeWindow(self):
        self.root = Tkinter.Tk()

        w = Tkinter.Label(self.root, text='hello!')
        w.pack()

        self.root.mainloop()

        return True
    
    



class MainWindowTests(unittest.TestCase):
    def testMakeWindow(self):
        mw = MainWindow()
        self.failUnless(mw.makeWindow())
    

def main():
    unittest.main()

        
if __name__ == '__main__':
    main()
