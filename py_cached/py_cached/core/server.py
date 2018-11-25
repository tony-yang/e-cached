import logging, py_cached.settings
logger = logging.getLogger(__name__)

import os
import socket

from py_cached.core.cache import Cache

class CacheServer:
    def __init__(self):
        logger.info('Create a new Cache Server object')
        print('Create a new Cache Server')
        self.server_address = '/tmp/uds_socket'
        self.connection_limit = 1
        self.exit = False
        self.buffer_size = 256
        self.cache = Cache()

        self.sock = self.create_server()
        self.start_server(self.sock, self.cache)

    def create_server(self):
        try:
            os.unlink(self.server_address)
        except OSError:
            if os.path.exists(self.server_address):
                logger.info('ERROR: Failed to clear old Unix Domain Socket')
                raise
        sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        sock.bind(self.server_address)
        sock.listen(self.connection_limit)
        logger.info('Starting on server {} with a maximum of {} connection'.format(self.server_address, self.connection_limit))
        print('Starting on server {} with a maximum of {} connection'.format(self.server_address, self.connection_limit))
        return sock

    def serve_request(self, command, cache):
        if command.decode().upper().startswith('SET'):
            print('### Cache a with b')
            cache.set('a', 'b')
        elif command.decode().upper().startswith('GET'):
            print('### Get cache with key a')
            value = cache.get('a')
            return value

    def start_server(self, sock, cache):
        logger.info('Starting the cache server')
        while not self.exit:
            connection, client_address = sock.accept()
            try:
                print('Connection from {}'.format(client_address))
                logger.info('Connection from {}'.format(client_address))
                while True:
                    data = connection.recv(self.buffer_size)
                    print('# Received {!r}'.format(data))
                    if data:
                        return_value = self.serve_request(data, cache)
                        print('# Return {}'.format(return_value))
                        if not return_value:
                            return_value = '#'
                        connection.sendall(return_value.encode())
                    else:
                        break
            except Exception as err:
                print('ERROR: {}'.format(err))
                logger.info('ERROR: {}'.format(err))
            finally:
                connection.close()