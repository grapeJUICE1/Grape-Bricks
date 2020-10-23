from Game.Shared import *

class Pad(GameObject):

    def __init__(self , position , sprite):
        super(Pad, self).__init__(position, GameConstant.PAD_SIZE, sprite)

    def setPosition(self , position):
        newPosition = [position[0] , position[1]]
        size = self.getSize()

        if newPosition[0] + size[0] >= GameConstant.SCREEN_SIZE[0]:
            newPosition[0] = GameConstant.SCREEN_SIZE[0] - size[0]

        super(Pad, self).setPosition(newPosition)
