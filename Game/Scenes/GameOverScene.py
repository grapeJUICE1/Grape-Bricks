import pygame
from Game.Scenes.Scene import *
from Game.Shared import GameConstant
from Game import Highscore

class GameOverScene(Scene):

     def __init__(self, game):
         super(GameOverScene, self).__init__(game)
         self.__playerName = ""
         self.__highScoreSprite = pygame.transform.scale(pygame.image.load(GameConstant.SPRITE_HIGHSCORE) , (276,164))

     def render(self):

        self.getGame().screen.blit( self.__highScoreSprite , (50 , 50))

        self.clearText()
        self.addText("Press F1 to restart the game" , (GameConstant.SCREEN_SIZE[0]/2) , (GameConstant.SCREEN_SIZE[1]/2)  , size = 40)

        self.addText("Your Name: " , 300 , 200 , size=30)
        self.addText(self.__playerName , 420 , 200 , size=30)

        super(GameOverScene, self).render()
     def handleEvents(self , events):
        super(GameOverScene,self).handleEvents(events)

        for event in events:
            keys = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                quit()
            if keys[pygame.K_F1]:
                self.getGame().reset()
                self.getGame().changeScene(GameConstant.PLAYING_SCENE)
            if keys[pygame.K_RETURN]:
                game = self.getGame()
                Highscore().add(self.__playerName, game.getScore())
                game.reset()
                game.changeScene(GameConstant.HIGH_SCORE_SCENE)

            elif event.type == pygame.KEYDOWN:
                currKey = event.key
                if currKey >= 65 and currKey <= 122:
                    self.__playerName += chr(currKey)
                elif event.key == pygame.K_BACKSPACE:
                    st =  self.__playerName
                    st = st[:-1]
                    self.__playerName = st
