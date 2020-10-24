import pygame
from Game.Scenes.Scene import Scene
from Game.Shared import GameConstant

class MenuScene(Scene):

    def __init__(self, game):
         super(MenuScene, self).__init__(game)

         self.addText("F1: Start The Game" , x = 400 , y = 200 , size=30)
         self.addText("F2: See HighScores" , x = 400 , y = 250 , size=30)
         self.addText("F3: Exit" , x = 400 , y = 300 , size=30)

         self.__menuSprite = pygame.transform.scale(pygame.image.load(GameConstant.SPRITE_MENU) , GameConstant.SPRITE_MENU_SIZE)

    def render(self):
        self.getGame().screen.blit(self.__menuSprite , (50,50))
        super(MenuScene, self).render()

    def handleEvents(self ,events):
        # super(MenuScene, self).handleEvents(events)

        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_F1]:
                self.getGame().changeScene(GameConstant.PLAYING_SCENE)

            if keys[pygame.K_F2]:
                self.getGame().changeScene(GameConstant.HIGH_SCORE_SCENE)

            if keys[pygame.K_F3]:
                pygame.quit()


