#!/usr/bin/env python
import logging, py_cached.settings
logger = logging.getLogger(__name__)

from py_cached.core.client import CacheClient

def main():
    logger.info('Calling cached main()')
    print('Welcome to ecache!')
    cs = CacheClient()
    while True:
        if not cs:
            cs = CacheClient()
        command = input('> ')
        print('Command = {}'.format(command))
        command.strip()
        if command.lower() == 'quit' or command.lower() == 'exit':
            break

        cs.send_command(command)

if __name__ == '__main__':
    main()
