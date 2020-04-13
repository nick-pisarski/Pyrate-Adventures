import logging
import os

import pygame

from .entity import Entity

log = logging.getLogger(os.path.basename(__file__))

class Player(Entity):
    """Representing the player as a pirate ship
    """
    speed = 5
    facing = -1
    buffer = 25
    image_url = 'images/player/PirateShip64.png'

    def __init__(self, screen):
        super().__init__(screen)
        self.image = pygame.image.load(self.image_url)
        self.rect = self.image.get_rect()

        #  Set initial postion
        self.rect.move_ip(50, self.facing*self.speed)

    def move(self, direction):
        if direction:
            self.facing = direction
        self.rect.move_ip(0, direction*self.speed)
        if self.rect.bottom >= self.screen_rect.bottom - self.buffer:
            self.rect.bottom = self.screen_rect.bottom - self.buffer
        if self.rect.top <= self.screen_rect.top + self.buffer:
            self.rect.top = self.screen_rect.top + self.buffer

    def blitme(self):
        """draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)
