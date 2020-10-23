import pygame
from Game.Bricks import Brick
from Game.Shared import GameConstant

class SpeedBrick(Brick):
    def __init__(self , position , sprite , game):
        super(SpeedBrick, self).__init__(position , sprite , game)

    def hit(self):
        balls = self.getGame().getBalls()
        for ball in balls:
            ball.setSpeed(ball.getSpeed()+1)

        super(SpeedBrick, self).hit()

    def getHitSound(self):
        return GameConstant.SOUND_HIT_BRICK_SPEED
