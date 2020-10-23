import os
from random import choice
import fileinput
import pygame

import solveModuleNotFoundError
from Game.Shared import *
from Game.Bricks import *

class Level(GameObject):

    def __init__(self , game):
        self.__game = game
        self.__bricks = []
        self.__amountOfBricksLeft = 0
        self.__currentLevel = 0

    def getBricks(self):
        return self.__bricks

    def getAmountOfBricksLeft(self):
        return self.__amountOfBricksLeft

    def brickHit(self):
        self.__amountOfBricksLeft -= 1

    def loadNextLevel(self):
        pass

    def load(self , level):
        self.__currentLevel = 0
        x,y = 0,0
        for line in fileinput.input(os.path.join("Assets" , "Levels" , "level"+str(self.__currentLevel)+".dat")):
            for brick in line:
                if brick == "1":
                    brick = choice(["Green" , "Red" ,"Purple"])
                    brick = Brick((x,y) , pygame.transform.scale(pygame.image.load(os.path.join("Assets" , f"{brick}.png")) , GameConstant.BRICK_SIZE) , self.__game , brick)
                    self.__bricks.append(brick)
                    self.__amountOfBricksLeft += 1

                elif brick == "2":
                    brick = SpeedBrick((x,y) , pygame.transform.scale(pygame.image.load(GameConstant.SPRITE_SPEED_BRICK) , GameConstant.BRICK_SIZE) , self.__game)
                    print(brick.getSprite())
                    self.__bricks.append(brick)
                    self.__amountOfBricksLeft += 1

                elif brick == "3":
                    brick = LifeBrick((x,y) , pygame.transform.scale(pygame.image.load(GameConstant.SPRITE_LIFE_BRICK) , GameConstant.BRICK_SIZE) , self.__game)
                    self.__bricks.append(brick)
                    self.__amountOfBricksLeft += 1

                x += GameConstant.BRICK_SIZE[0]

            x = 0
            y += GameConstant.BRICK_SIZE[1]
