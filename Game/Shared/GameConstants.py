import os

class GameConstant:
    BG = os.path.join("Assets" , "background.png")
    SPRITE_STADARD_BRICK = os.path.join("Assets" , "Green.png")
    SPRITE_LIFE_BRICK = os.path.join("Assets" , "life.png")
    SPRITE_SPEED_BRICK = os.path.join("Assets" , "speed.png")
    SPRITE_BALL = os.path.join("Assets" , "ball.png")
    SPRITE_PAD = os.path.join("Assets" , "pad.png")
    SPRITE_MENU = os.path.join("Assets" , "Menu.png")
    SPRITE_MENU_SIZE = (276,276)
    SPRITE_HIGHSCORE = os.path.join("Assets", "highscore.png")

    BRICK_SIZE = (40 , 25)
    SMALL_BRICK_SIZE = (20 , 25)
    BALL_SIZE = (11 , 11)
    PAD_SIZE = [130 , 13]
    SCREEN_SIZE = (840 , 600)

    BALL_SPEED  = 3

    PLAYING_SCENE = 0
    GAME_OVER_SCENE = 1
    HIGH_SCORE_SCENE = 2
    MENU_SCENE = 3

    SOUND_FILE_HIT_BRICK = os.path.join("Assets", "BrickHit.wav")
    SOUND_FILE_HIT_BRICK_LIFE = os.path.join("Assets", "ExtraLife.wav")
    SOUND_FILE_HIT_BRICK_SPEED = os.path.join("Assets", "SpeedUp.wav")
    SOUND_FILE_HIT_WALL = os.path.join("Assets", "WallBounce.wav")
    SOUND_FILE_HIT_PAD = os.path.join("Assets", "PadBounce.wav")
    SOUND_FILE_GAMEOVER = os.path.join("Assets", "GameOver.wav")

    SOUND_GAMEOVER = 0
    SOUND_HIT_BRICK = 1
    SOUND_HIT_BRICK_LIFE = 2
    SOUND_HIT_BRICK_SPEED = 3
    SOUND_HIT_WALL = 4
    SOUND_HIT_PAD = 5
