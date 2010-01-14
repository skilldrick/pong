import math


class MovingObject:
    xvel = 0
    yvel = 0

    def startUp(self):
        self.yvel = -self.velocity

    def startDown(self):
        self.yvel = self.velocity

    def stop(self):
        self.xvel = 0
        self.yvel = 0
    
    def move(self):
        x1, y1, x2, y2 = self.board.coords(self.id)
        newcoords = (x1 + self.xvel,
                     y1 + self.yvel,
                     x2 + self.xvel,
                     y2 + self.yvel)
        self.board.coords(self.id, newcoords)

        
class Paddle(MovingObject):
    velocity = 2
    
    def __init__(self, board, originX):
        self.board = board
        width = 5
        height = 40
        originY = 50
        self.id = self.board.create_rectangle(
            (originX, originY,
             originX + width, originY + height),
            fill='black')
    

class PaddleL(Paddle):
    def __init__(self, board):
        Paddle.__init__(self, board, 10)

        
class PaddleR(Paddle):
    def __init__(self, board):
        Paddle.__init__(self, board, 90)

        
class Ball(MovingObject):
    velocity = 0.5
    angle = math.pi / 4
    
    def __init__(self, board):
        self.board = board
        width = 5
        height = 5
        originX = 40
        originY = 10
        self.id = self.board.create_rectangle(
            (originX, originY,
             originX + width, originY + height),
            fill='black')

    def calcVelocity(self):
        adj = math.cos(self.angle) * self.velocity
        opp = math.sin(self.angle) * self.velocity
        self.xvel = adj
        self.yvel = opp

    def move(self):
        self.calcVelocity()
        MovingObject.move(self)

    def stop(self):
        self.velocity = 0
        
    def rotate(self):
        self.angle += math.pi / 4

    def checkCollision(self):
        x1, y1, x2, y2 = self.board.coords(self.id)
        if x2 > 80 or y2 > 80:
            self.stop()
