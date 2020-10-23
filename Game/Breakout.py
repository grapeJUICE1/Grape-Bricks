import pygame
import solveModuleNotFoundError
from Game import *
from Game.Scenes import *
from Game.Shared import *

class Breakout:
    def __init__(self):
        self.__lives = 1
        self.__score = 0

        self.__level  = Level(self)
        self.__level.load(0)

        self.__pad = Pad((GameConstant.SCREEN_SIZE[0]/2,GameConstant.SCREEN_SIZE[1] - GameConstant.PAD_SIZE[1]),pygame.image.load(GameConstant.SPRITE_PAD))
        self.__balls = [
            Ball((400,400) , pygame.transform.scale(pygame.image.load(GameConstant.SPRITE_BALL) , GameConstant.BALL_SIZE) ,self)
                    ]

        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption("Brick Breaker")
        pygame.mouse.set_visible(0)

        self.__clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode(GameConstant.SCREEN_SIZE , pygame.DOUBLEBUF, 32)
        self.bg = pygame.transform.scale(pygame.image.load(GameConstant.BG).convert_alpha() , GameConstant.SCREEN_SIZE)

        self.__scenes = (
            PlayingGameScene(self),
            GameOverScene(self),
            HighscoreScene(self),
            MenuScene(self)

            )
        self.__currentScene = 0
        self.__sounds = (
            pygame.mixer.Sound(GameConstant.SOUND_FILE_GAMEOVER),
            pygame.mixer.Sound(GameConstant.SOUND_FILE_HIT_BRICK),
            pygame.mixer.Sound(GameConstant.SOUND_FILE_HIT_BRICK_LIFE),
            pygame.mixer.Sound(GameConstant.SOUND_FILE_HIT_BRICK_SPEED),
            pygame.mixer.Sound(GameConstant.SOUND_FILE_HIT_WALL),
            pygame.mixer.Sound(GameConstant.SOUND_FILE_HIT_PAD)
        )


    def start(self):
        while 1:
            self.__clock.tick(60)
            self.screen.fill((0,0,0))
            self.screen.blit( self.bg, (0,0))

            currentScene = self.__scenes[self.__currentScene]
            currentScene.handleEvents(pygame.event.get())
            currentScene.render()

            pygame.display.update()

    def changeScene(self , scene):
        self.__currentScene = scene

    def getLevel(self):
        return self.__level

    def getLives(self):
        return self.__lives
    def getScore(self):
        return self.__score

    def getBalls(self):
        return self.__balls

    def getPad(self):
        return self.__pad

    def playSound(self, soundClip):
        sound = self.__sounds[soundClip]

        sound.stop()
        sound.play()

    def increaseScore(self , score):
        self.__score += score

    def increaseLives(self):
        self.__lives += 1

    def reduceLives(self):
        self.__lives -= 1
    def reset(self):
        self.__score = 0
        self.__lives = 5
        self.__level.load(0)

Breakout().start()
