#!v-env/bin/python
import logging
from os import path

logging.basicConfig(
    level=logging.INFO,
    format="(%(asctime)s) %(name)s:  %(message)s",
    datefmt="%m.%d.%y@%H:%M:%S",
)

log = logging.getLogger(path.basename(__file__))
def main():
    log.info('It works')

if __name__ == "__main__":
    main()
