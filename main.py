#!v-env/bin/python
import logging
import os
import sys
from random import randint

import pygame

from lib.entity import EntityConfig, Floater, Player
from lib.settings import GameSettings

logging.basicConfig(
    level=logging.INFO,
    format="(%(asctime)s) %(name)s:  %(message)s",
    datefmt="%m.%d.%y@%H:%M:%S",
)
log = logging.getLogger(os.path.basename(__file__))

FLOATER_PATH = "images/Crate64.png"
PLAYER_PATH = "images/player/PirateShip64.png"


def end_game():
    pygame.quit()
    sys.exit()


def main():
    # Initiate game
    pygame.init()
    clock = pygame.time.Clock()

    # Setting up screen
    settings = GameSettings(1280, 960)
    screen = pygame.display.set_mode(settings.screen_size)
    pygame.display.set_caption("Py-rate Adventures")

    player = Player(EntityConfig(PLAYER_PATH, 5, 25), screen)
    floater = Floater(EntityConfig(FLOATER_PATH, 5, 15), screen)

    while True:
        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end_game()

        # Updates
        keystate = pygame.key.get_pressed()

        if keystate[pygame.K_q]:
            end_game()

        direction = keystate[pygame.K_s] - keystate[pygame.K_w]
        player.move(direction)
        floater.move()

        # Visuals
        screen.fill(settings.background_color)
        player.blitme()
        if floater is not None:
            floater.blitme()
        else:
            speed = randint(5, 50)
            floater = Floater(EntityConfig(FLOATER_PATH, 5, speed), screen)

        pygame.display.flip()
        clock.tick(settings.frame_rate)


if __name__ == "__main__":
    try:
        main()
    except SystemExit as ex:
        log.info("System Exit")
