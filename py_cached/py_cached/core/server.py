import logging, py_cached.settings
logger = logging.getLogger(__name__)

import os
import socket

from py_cached.core.cache import Cache

class CacheServer:
    def __init__(self, exit=False):
        logger.info('Create a new Cache Server object')
        self.server_address = '/tmp/uds_socket'
        self.connection_limit = 1
        self.exit = exit
        self.buffer_size = 256
        self.cache = Cache()

        self.sock = self.create_server()
        self.start_server(self.sock, self.cache)

    def create_server(self):
        try:
            os.unlink(self.server_address)
        except OSError:
            if os.path.exists(self.server_address):
                logger.error('ERROR: Failed to clear old Unix Domain Socket')
                raise
        sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        sock.bind(self.server_address)
        sock.listen(self.connection_limit)
        logger.info('Starting on server {} with a maximum of {} connections'.format(self.server_address, self.connection_limit))
        print('Starting on server {} with a maximum of {} connections'.format(self.server_address, self.connection_limit))
        return sock

    def serve_request(self, command, cache):
        if isinstance(command, str):
            command_string = command.strip().split()
        else:
            command_string = command.decode().strip().split()
        action = command_string[0].upper().strip()

        if action == 'SET':
            if len(command_string) != 3:
                raise Exception('Expect both the key and the value are provided to the `SET` action')
            key = command_string[1]
            value = command_string[2]
            logger.debug('SET: Cache `{}` with `{}`'.format(key, value))
            cache.set(key, value)
        elif action == 'GET':
            if len(command_string) != 2:
                raise Exception('Expect only the key is provided to the `GET` action')
            key = command_string[1]
            logger.debug('GET: Get cache with key `{}`'.format(key))
            value = cache.get(key)
            return value

    def start_server(self, sock, cache):
        logger.info('Starting the cache server')
        print('Starting the Cache Server')
        while not self.exit:
            connection, client_address = sock.accept()
            try:
                print('Connection from {}'.format(client_address.decode()))
                logger.info('Connection from: {}'.format(client_address.decode()))
                while True:
                    data = connection.recv(self.buffer_size)
                    logger.debug('SERVER: Received `{}`'.format(data.decode()))
                    print('SERVER: Received `{}`'.format(data.decode()))
                    return_value = None
                    if data:
                        try:
                            return_value = self.serve_request(data, cache)
                            logger.debug('SERVER: Return value `{}`'.format(return_value.decode()))
                            print('SERVER: Return value `{}`'.format(return_value.decode()))
                        except:
                            next
                        if not return_value:
                            return_value = '#'
                        connection.sendall(return_value.encode())
                    else:
                        break
            except Exception as err:
                print('ERROR: {}'.format(err))
                logger.error('ERROR: {}'.format(err))
            finally:
                connection.close()

    def shutdown_server(self):
        if self.sock.fileno() > 0:
            self.sock.close()
