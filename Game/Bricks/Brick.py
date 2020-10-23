from Game.Shared import GameObject
from Game.Shared import GameConstant

class Brick(GameObject):
    def __init__(self , position , sprite , game):
        self.__game = game
        self.__hitpoints = 100
        self.__lives = 1
        super(Brick, self).__init__(position , GameConstant.BRICK_SIZE , sprite)

    def getGame(self):
        return self.__game

    def isDestroyed(self):
        return self.__lives <= 0

    def getHitPoints(self):
        return self.__hitpoints

    def hit(self):
        self.__lives -= 1

    def getHitSound(self):
        return GameConstant.SOUND_HIT_BRICK
