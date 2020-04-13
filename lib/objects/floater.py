import logging
import os
import random

import pygame

from .entity import Entity

log = logging.getLogger(os.path.basename(__file__))


class Floater(Entity):

    img_url = 'images/Crate64.png'
    speed = 5
    buffer = 15

    def __init__(self, screen):
        super().__init__(screen)
        self.image = pygame.image.load(self.img_url)
        self.rect = self.image.get_rect()
        self.reset()

    def move(self):
        self.rect.move_ip(-self.speed, 0)
        if self.is_offscreen():
            self.reset()

    def blitme(self):
        """Draw the entity at its current location"""
        self.screen.blit(self.image, self.rect)

    def reset(self):
        """Resets entity back to default position"""
        x = self.screen_rect.right - (self.rect.width + self.buffer)
        y = random.randint(1, self.screen_rect.height - self.rect.height - self.buffer)
        self.rect.center = (x, y)
