from Game.Shared import GameObject
from Game.Shared import GameConstant

class Brick(GameObject):
    def __init__(self , position , sprite , game , color=None):
        self.__color = color
        self.__game = game
        self.__hitpoints = 100
        self.__lives = 1
        self.__timesHit = 0
        super(Brick, self).__init__(position , GameConstant.BRICK_SIZE , sprite)

    def getGame(self):
        return self.__game

    def isDestroyed(self):
        return self.__lives <= 0

    def getHitPoints(self):
        return self.__hitpoints

    def increseHit(self):
        self.__timesHit += 1

    def getTimeHit(self):
        return self.__timesHit

    def hit(self):
        self.__lives -= 1

    def getHitSound(self):
        return GameConstant.SOUND_HIT_BRICK

    def getColor(self):
        return self.__color
