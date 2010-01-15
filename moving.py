import math


class MovingObject:
    xvel = 0
    yvel = 0

    def __init__(self, x, y, width, height):
        self.coords = (x, y, x + width, y + height)

    def startUp(self):
        self.yvel = -self.velocity

    def startDown(self):
        self.yvel = self.velocity

    def stop(self):
        self.xvel = 0
        self.yvel = 0

    def getCoords(self):
        return self.coords
    
    def move(self):
        x1, y1, x2, y2 = self.coords
        newCoords = (x1 + self.xvel,
                     y1 + self.yvel,
                     x2 + self.xvel,
                     y2 + self.yvel)
        self.coords = newCoords

        
class Paddle(MovingObject):
    velocity = 2
    
    def __init__(self, originX):
        width = 5
        height = 40
        originY = 50
        MovingObject.__init__(self,
                              originX,
                              originY,
                              width,
                              height)
    

class PaddleL(Paddle):
    def __init__(self):
        Paddle.__init__(self, 10)

        
class PaddleR(Paddle):
    def __init__(self):
        Paddle.__init__(self, 90)

        
class Ball(MovingObject):
    velocity = 0.5
    angle = math.pi / 4
    
    def __init__(self):
        width = 5
        height = 5
        originX = 40
        originY = 10
        MovingObject.__init__(self,
                              originX,
                              originY,
                              width,
                              height)

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
