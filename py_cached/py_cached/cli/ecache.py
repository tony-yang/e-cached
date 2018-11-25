#!/usr/bin/env python
import logging, py_cached.settings
logger = logging.getLogger(__name__)

import argparse
from py_cached.core.client import CacheClient

def main():
    logger.info('Calling cached main()')
    cs = CacheClient()
    cs.send_command('SET a abc')
    cs.send_command('GET a')

if __name__ == '__main__':
    main()
