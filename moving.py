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
    
    def move(self, backwards=False):
        x1, y1, x2, y2 = self.coords
        xvel, yvel = self.xvel, self.yvel
        if backwards:
            xvel = -xvel
            yvel = -yvel
        newCoords = (x1 + xvel,
                     y1 + yvel,
                     x2 + xvel,
                     y2 + yvel)
        self.coords = newCoords

    def bounce(self, side):
        self.move(True)

        
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
    velocity = math.sqrt(2)
    angle = math.pi / 5
    
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

    def move(self, backwards=False):
        self.calcVelocity()
        MovingObject.move(self, backwards)

    def stop(self):
        self.velocity = 0

    def normaliseAngle(self):
        while self.angle > math.pi * 2:
            self.angle -= math.pi * 2
        while self.angle < -math.pi * 2:
            self.angle += math.pi * 2
        
    def bounce(self, side):
        print(side)
        self.move(True)
        if side == 'left' or side == 'right':
            self.angle = math.pi - self.angle
        else:
            self.angle = -self.angle
        self.normaliseAngle()

