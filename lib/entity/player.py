import logging
import os

from pygame import image
from pygame.surface import Surface

from lib.entity.entity_config import EntityConfig

from .entity import Entity

log = logging.getLogger(os.path.basename(__file__))


class Player(Entity):
    """Representing the player as a pirate ship"""

    def __init__(self, config: EntityConfig, screen: Surface):
        self.config = config
        self.screen = screen
        self.image = image.load(self.config.image_url)
        self.image_rect = self.image.get_rect()

        #  Set initial postion
        self.image_rect.move_ip(50, self.screen.get_height() / 2)

    def move(self, direction):
        screen_rect = self.screen.get_rect()

        if direction:
            self.facing = direction
        self.image_rect.move_ip(0, direction * self.config.speed)
        if self.image_rect.bottom >= screen_rect.bottom - self.config.padding:
            self.image_rect.bottom = screen_rect.bottom - self.config.padding
        if self.image_rect.top <= screen_rect.top + self.config.padding:
            self.image_rect.top = screen_rect.top + self.config.padding
