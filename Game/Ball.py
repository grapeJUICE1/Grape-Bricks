import solveModuleNotFoundError
import pygame
from Game.Shared import *

class Ball(GameObject):
    def __init__(self , position , sprite , game):
        self.__game = game
        self.__speed = GameConstant.BALL_SPEED
        self.__increment = [2 , 2]
        self.__direction = [1,1]
        self.__inMotion = 0

        super(Ball, self).__init__(position, GameConstant.BALL_SIZE, sprite)

    def setSpeed(self , newSpeed):
        self.__speed = newSpeed

    def resetSpeed(self):
        self.__speed = GameConstant.BALL_SPEED

    def getSpeed(self):
        return self.__speed

    def isInMotion(self):
        return self.__inMotion

    def setMotion(self , isMoving):
        self.__inMotion = isMoving
        self.resetSpeed()

    def changeDirection(self, gameObject):

        position = self.getPosition()
        size = self.getSize()
        objectPosition = gameObject.getPosition()
        objectSize = gameObject.getSize()

        if position[1] > objectPosition[1] and \
                        position[1] < objectPosition[1] + objectSize[1] and \
                        position[0] > objectPosition[0] and\
                        position[0] < objectPosition[0] + objectSize[0]:
            self.setPosition((position[0], objectPosition[1] + objectSize[1]))
            self.__direction[1] *= -1

        elif position[1] + size[1] > objectPosition[1] and \
                                position[1] + size[1] < objectPosition[1] + objectSize[1] and \
                        position[0] > objectPosition[0] and \
                        position[0] < objectPosition[0] + objectSize[0]:
            self.setPosition((position[0], objectPosition[1] - objectSize[1]))
            self.__direction[1] *= -1

        elif position[0] + size[0] > objectPosition[0] and \
                                position[0] + size[0] < objectPosition[0] + objectSize[0]:
            self.setPosition((objectPosition[0] - size[0], position[1]))
            self.__direction[0] *= -1

        else:
            self.setPosition((objectPosition[0] + objectSize[0], position[1]))
            self.__direction[0] *= -1
            self.__direction[1] *= -1

    def updatePosition(self):
        if not self.isInMotion():
            padPosition = self.__game.getPad().getPosition()
            self.setPosition((
                padPosition[0]+ (GameConstant.PAD_SIZE[0] / 2) ,
                GameConstant.SCREEN_SIZE[1] - GameConstant.PAD_SIZE[1] - GameConstant.BALL_SIZE[1]
                 ))
            return


        position = self.getPosition()
        size = self.getSize()

        newPosition = [position[0] + (self.__increment[0] * self.__speed) * self.__direction[0],
                       position[1] + (self.__increment[1] * self.__speed) * self.__direction[1]]

        if newPosition[0] + size[0] >= GameConstant.SCREEN_SIZE[0]:
            self.__direction[0] *= -1
            newPosition = [GameConstant.SCREEN_SIZE[0] - size[0], newPosition[1]]
            self.__game.playSound(GameConstant.SOUND_HIT_WALL)


        if newPosition[0] <= 0:
            self.__direction[0] *= -1
            newPosition = [0, newPosition[1]]
            self.__game.playSound(GameConstant.SOUND_HIT_WALL)

        if newPosition[1] + size[1] >= GameConstant.SCREEN_SIZE[1]:
            self.__direction[1] *= -1
            newPosition = [newPosition[0], GameConstant.SCREEN_SIZE[1] - size[1]]
            self.__game.playSound(GameConstant.SOUND_HIT_WALL)


        if newPosition[1] <= 0:
            self.__direction[1] *= -1
            newPosition = [newPosition[0], 0]
            self.__game.playSound(GameConstant.SOUND_HIT_WALL)


        self.setPosition(newPosition)

    def isBallDead(self):
        pos = self.getPosition()
        size = self.getSize()

        if pos[1] + size[1] >= GameConstant.SCREEN_SIZE[1]:
            return 1

        return 0
