import pygame
from Game.Scenes.Scene import Scene
from Game.Shared import GameConstant

class PlayingGameScene(Scene):

    def __init__(self, game):
         super(PlayingGameScene, self).__init__(game)


    def render(self):
        super(PlayingGameScene,self).render()

        game = self.getGame()
        if game.getLives() <= 0:
            game.playSound(GameConstant.SOUND_GAMEOVER)
            game.changeScene(GameConstant.GAME_OVER_SCENE)
            return
        pad = game.getPad()

        for ball in game.getBalls():
            ball.updatePosition()

            for brick in game.getLevel().getBricks():
                if not brick.isDestroyed() and ball.intersects(brick):
                    game.playSound(brick.getHitSound())
                    brick.hit()
                    game.increaseScore(brick.getHitPoints())
                    ball.changeDirection(brick)
                    break

            if ball.intersects(pad):
                game.playSound(GameConstant.SOUND_HIT_PAD)
                ball.changeDirection(pad)

            if ball.isBallDead():
                ball.setMotion(0)
                game.reduceLives()

            game.screen.blit(ball.getSprite() , ball.getPosition())

        for brick in game.getLevel().getBricks():
            if not brick.isDestroyed():
                game.screen.blit(brick.getSprite() , brick.getPosition())


        pad.setPosition((pygame.mouse.get_pos()[0] , pad.getPosition()[1]))
        game.screen.blit(pad.getSprite() , pad.getPosition())

        self.clearText()

        self.addText(f"Your Score is {game.getScore()}" , x = 1 , y = GameConstant.SCREEN_SIZE[1] - 60 )
        self.addText(f"Your Lives is {game.getLives()}" , x = 1 , y = GameConstant.SCREEN_SIZE[1] - 30 )

    def handleEvents(self , events):
        super(PlayingGameScene,self).handleEvents(events)

        for event in events:
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                balls = self.getGame().getBalls()

                for ball in balls:
                    ball.setMotion(1)

