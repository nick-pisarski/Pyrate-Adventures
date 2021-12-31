from abc import abstractmethod
from typing import Protocol

from pygame.surface import Surface
from pygame.rect import Rect

from lib.entity.entity_config import EntityConfig

class Entity(Protocol):
    """Representing an entity on the screen"""

    config: EntityConfig
    screen: Surface
    image: Surface
    image_rect: Rect

    def is_offscreen(self):
        """True or False if entity is completely off the screen

        Returns:
            boolean
        """
        screen_rect = self.screen.get_rect()
        return (
            self.image_rect.right <= 0
            or self.image_rect.bottom <= 0
            or self.image_rect.top >= screen_rect.bottom
            or self.image_rect.left >= screen_rect.right
        )

    @abstractmethod
    def move(self, direction: int) -> None:
        raise NotImplementedError

    def blitme(self) -> None:
        self.screen.blit(self.image, self.image_rect)
