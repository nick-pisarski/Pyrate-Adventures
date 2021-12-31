#!v-env/bin/python
import logging
import os
import sys

import pygame

from lib.objects import Floater, Player
from lib.settings import GameSettings

logging.basicConfig(
    level=logging.INFO,
    format="(%(asctime)s) %(name)s:  %(message)s",
    datefmt="%m.%d.%y@%H:%M:%S",
)
log = logging.getLogger(os.path.basename(__file__))


def main():
    # Initiate game
    pygame.init()
    clock = pygame.time.Clock()

    # Setting up screen
    settings = GameSettings(1280, 960)
    screen = pygame.display.set_mode(settings.screen_size)
    pygame.display.set_caption("Py-rate Adventures")

    player = Player(screen)
    floater = Floater(screen)

    while True:
        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Updates
        keystate = pygame.key.get_pressed()
        direction = keystate[pygame.K_s] - keystate[pygame.K_w]
        player.move(direction)
        floater.move()

        # Visuals
        screen.fill(settings.background_color)
        player.blitme()
        if floater is not None:
            floater.blitme()
        else:
            floater = Floater(screen)

        pygame.display.flip()
        clock.tick(settings.frame_rate)


if __name__ == "__main__":
    try:
        main()
    except SystemExit as ex:
        log.info("System Exit")
