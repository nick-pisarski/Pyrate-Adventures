import pygame


class GameSettings():
    """ Represents the settings for the game
    """

    def __init__(self, width, height):
        self.height = height
        self.width = width
        self.screen_size = (width, height)
        self.background_color = pygame.Color(1, 120, 189)
        self.frame_rate = 60
