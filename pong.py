import Tkinter

class MainWindow:
    def __init__(self):
        self.root = Tkinter.Tk()

        w = Tkinter.Label(self.root, text='hello!')
        w.pack()

        self.root.mainloop()


def main():
    x = MainWindow()

        
if __name__ == '__main__':
    main()
