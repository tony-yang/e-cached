#!/usr/bin/env python
import logging, py_cached.settings
logger = logging.getLogger(__name__)

from py_cached.core.server import CacheServer

def main():
    logger.info('Calling cached main()')
    cs = CacheServer()

if __name__ == '__main__':
    main()
