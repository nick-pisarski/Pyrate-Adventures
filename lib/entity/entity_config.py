from dataclasses import dataclass


@dataclass
class EntityConfig:
    """
    A dataclass for configuring Entity Objects

    image_url: str -> location of image to be rendered
    speed: int -> number of pixels moved per frame
    padder: int -> number of pixels around entity
    """

    image_url: str
    speed: int
    padding: int
