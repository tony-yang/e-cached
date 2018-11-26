import logging, py_cached.settings
logger = logging.getLogger(__name__)

import socket
import sys

class CacheClient:
    def __init__(self):
        logger.info('Create a new Cache Client object')
        self.server_address = '/tmp/uds_socket'
        self.buffer_size = 256
        self.sock = self.connect()

    def connect(self):
        sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        logger.info('Connecting to {}'.format(self.server_address))
        print('Connecting to {}'.format(self.server_address))
        try:
            sock.connect(self.server_address)
        except socket.error as err:
            logger.error('ERROR: Client failed to connect to socket: {}'.format(err))
            print('ERROR: Client failed to connect to socket: {}'.format(err))
            sys.exit(1)
        return sock

    def send_command(self, command):
        try:
            command = command.encode()
            logger.debug('CLIENT: Command `{}`'.format(command.decode()))
            self.sock.sendall(command)
            return_value = self.sock.recv(self.buffer_size)
            if return_value and return_value.decode() != '#':
                print('{}'.format(return_value.decode()))
            return return_value
        except socket.error as err:
            logger.error('ERROR: Closing socket due to error: {}'.format(err))
            print('ERROR: Closing socket due to error: {}'.format(err))
            self.sock.close()
