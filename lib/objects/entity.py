import logging
import os

import pygame

log = logging.getLogger(os.path.basename(__file__))


class Entity:
    """Representing an entity on the screen"""

    rect = None

    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()

    def is_offscreen(self):
        """True or False if self.Rect is completely off the screen

        Returns:
            boolean
        """
        return (
            self.rect.right <= 0
            or self.rect.bottom <= 0
            or self.rect.top >= self.screen_rect.bottom
            or self.rect.left >= self.screen_rect.right
        )

    def move(self, direction):
        raise NotImplementedError

    def blitme(self):
        raise NotImplementedError
