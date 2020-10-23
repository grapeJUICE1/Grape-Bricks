import pygame
from Game.Scenes.Scene import *
from Game.Shared import GameConstant
from Game import Highscore

class HighscoreScene(Scene):

    def __init__(self, game):
         super(HighscoreScene, self).__init__(game)
         self.__highScoreSprite = pygame.transform.scale(pygame.image.load(GameConstant.SPRITE_HIGHSCORE) , (276,164))

    def render(self):
        self.getGame().screen.blit(self.__highScoreSprite , (50 , 50))

        self.clearText()

        highscore = Highscore()

        x = 350
        y = 100
        for score in highscore.getScores():
            self.addText(score[0] , x , y , size = 30)
            self.addText(str(score[1]) , x + 200 , y , size = 30)

            y+=30

        self.addText("Press F1 to start The Game" , 50 , 300 , size = 30)

        super(HighscoreScene, self).render()


    def handleEvents(self , events):
        super(HighscoreScene,self).handleEvents(events)

        for event in events:
            keys = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                quit()
            if keys[pygame.K_F1]:
                self.getGame().reset()
                self.getGame().changeScene(GameConstant.PLAYING_SCENE)


