import logging
import os

from pygame import image
from pygame.surface import Surface

from .entity import Entity

log = logging.getLogger(os.path.basename(__file__))


class Player(Entity):
    """Representing the player as a pirate ship"""

    speed = 5
    facing = -1
    buffer = 25
    image_url = "images/player/PirateShip64.png"

    def __init__(self, screen: Surface):
        self.screen = screen
        self.image = image.load(self.image_url)
        self.image_rect = self.image.get_rect()

        #  Set initial postion
        self.image_rect.move_ip(50, self.facing * self.speed)

    def move(self, direction):
        screen_rect = self.screen.get_rect()

        if direction:
            self.facing = direction
        self.image_rect.move_ip(0, direction * self.speed)
        if self.image_rect.bottom >= screen_rect.bottom - self.buffer:
            self.image_rect.bottom = screen_rect.bottom - self.buffer
        if self.image_rect.top <= screen_rect.top + self.buffer:
            self.image_rect.top = screen_rect.top + self.buffer
