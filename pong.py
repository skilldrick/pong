from tkinter import *
from tkinter import ttk




def registerEvents(root):
    root.bind('<Key>', move)

def move(event):
    if event.keysym == 'Up':
        print('Up')
    elif event.keysym == 'Down':
        print('Down')

def main():
    root = Tk()

    scoreFrame = ttk.Frame(root,
                           borderwidth=3,
                           relief='sunken',
                           width=100, height=50)
    scoreFrame.grid()

    gameFrame = ttk.Frame(root,
                          borderwidth=3,
                          relief='sunken',
                          width=100, height=100)
    gameFrame.grid()

    registerEvents(root)
    
    root.mainloop()
    
        
if __name__ == '__main__':
    main()
