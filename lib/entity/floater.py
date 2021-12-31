import logging
import os
import random

from pygame import image
from pygame.surface import Surface

from .entity import Entity

logger = logging.getLogger(os.path.basename(__file__))


class Floater(Entity):

    img_url = "images/Crate64.png"
    speed = 5
    buffer = 15

    def __init__(self, screen: Surface):
        self.screen = screen
        self.image = image.load(self.img_url)
        self.image_rect = self.image.get_rect()
        self.reset()

    def move(self):
        x = -self.speed
        # logger.info(f'Moving over ({x}, 0)')
        self.image_rect.move_ip(x, 0)
        if self.is_offscreen():
            self.reset()

    def reset(self):
        """Resets entity back to default position"""
        screen_rect = self.screen.get_rect()
        x = screen_rect.right - (self.image_rect.width + self.buffer)
        y = random.randint(1, screen_rect.height - self.image_rect.height - self.buffer)
        logger.info(f"Resetting to ({x}, {y})")
        self.image_rect.center = (x, y)
