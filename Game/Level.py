import os
from random import choice
import fileinput
import random
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
        self.__currentLevel += 1
        fileName = os.path.join("Game", "Assets", "Levels", "level" + str(self.__currentLevel) + ".dat")

        if not os.path.exists(fileName):
            self.loadRandom()

        else:
            self.load(self.__currentLevel)
    def reset(self):
        self.__bricks = []
        self.__amountOfBricksLeft = 0
        self.__currentLevel = 0
    def load(self , level):
        print(int(GameConstant.SCREEN_SIZE[0] / GameConstant.BRICK_SIZE[0]))
        self.__bricks = []
        self.__currentLevel = 0
        x,y = 0,0
        for line in fileinput.input(os.path.join("Assets" , "Levels" , "level"+str(self.__currentLevel)+".dat")):
            for brick in line:
                if brick == "1":
                    color = choice(["Green" , "Red" ,"Purple" , "Blue" , "Golden" , "LightBlue" , "Yellow" , "DarkGreen" , "Grey" , "Brown"])
                    brick = Brick((x,y) , pygame.transform.scale(pygame.image.load(os.path.join("Assets" , f"{color}.png")) , GameConstant.BRICK_SIZE) , self.__game , color)
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
                elif brick == "4":
                    color = choice(["small-green" ,  "small-purple" , "small-red" , "small-blue"])
                    brick = Brick((x,y) , pygame.transform.scale(pygame.image.load(os.path.join("Assets" , f"{color}.png")) , GameConstant.SMALL_BRICK_SIZE) , self.__game)
                    self.__bricks.append(brick)
                    self.__amountOfBricksLeft += 1

                x += GameConstant.BRICK_SIZE[0]

            x = 0
            y += GameConstant.BRICK_SIZE[1]



    def loadRandom(self):
        self.__bricks = []

        x, y = 0, 0

        maxBricks = int(GameConstant.SCREEN_SIZE[0] / GameConstant.BRICK_SIZE[0])
        rows = random.randint(10, 15)


        amountOfSuperPowerBricks = 0
        for row in range(0, rows):
            for brick in range(0, maxBricks):
                brickType = random.randint(0, 4)
                if brickType == 1 and random.randint(1,3)== 2:
                    brickType == 4
                if brickType == 1 or (amountOfSuperPowerBricks >= 3 and brickType != 4):
                    color = choice(["Green" , "Red" ,"Purple" , "Blue" , "Golden" , "LightBlue" , "Yellow" , "DarkGreen" , "Grey" , "Brown"])
                    brick = Brick((x,y) , pygame.transform.scale(pygame.image.load(os.path.join("Assets" , f"{color}.png")) , GameConstant.BRICK_SIZE) , self.__game , color)
                    self.__bricks.append(brick)
                    self.__amountOfBricksLeft += 1

                elif brickType == 2:
                    brick = SpeedBrick((x,y) , pygame.transform.scale(pygame.image.load(GameConstant.SPRITE_SPEED_BRICK) , GameConstant.BRICK_SIZE) , self.__game)
                    print(brick.getSprite())
                    self.__bricks.append(brick)
                    self.__amountOfBricksLeft += 1
                    amountOfSuperPowerBricks += 1

                elif brickType == 3:
                    brick = LifeBrick((x,y) , pygame.transform.scale(pygame.image.load(GameConstant.SPRITE_LIFE_BRICK) , GameConstant.BRICK_SIZE) , self.__game)
                    self.__bricks.append(brick)
                    self.__amountOfBricksLeft += 1
                    amountOfSuperPowerBricks += 1
                elif brickType == 4:
                    color = choice(["small-green" ,  "small-purple" , "small-red" , "small-blue"])
                    brick = Brick((x,y) , pygame.transform.scale(pygame.image.load(os.path.join("Assets" , f"{color}.png")) , GameConstant.SMALL_BRICK_SIZE) , self.__game)
                    self.__bricks.append(brick)
                    self.__amountOfBricksLeft += 1


                x += GameConstant.BRICK_SIZE[0]

            x = 0
            y += GameConstant.BRICK_SIZE[1]
