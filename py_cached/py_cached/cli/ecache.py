#!/usr/bin/env python
import logging, py_cached.settings
logger = logging.getLogger(__name__)

from py_cached.core.client import CacheClient

def main():
    logger.info('Calling cached main()')
    print('Welcome to ecache!')

    cs = CacheClient()
    cs.send_command('SET a abc')
    cs.send_command('GET a')
    cs.send_command('SET d def')
    cs.send_command('GET d')
    cs.send_command('GET a')

if __name__ == '__main__':
    main()
