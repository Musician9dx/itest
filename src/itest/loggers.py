import logging as lg
import sys


def get_logger():
    lg.basicConfig(
        format='[%(asctime)s : %(levelname)s : %(module)s: %(message)s]',
        level=lg.INFO,
        handlers=[
            lg.FileHandler('log/logs.log'),
            lg.StreamHandler(sys.stdout)
        ]
    )

    logger=lg.getLogger('logger')

    return logger