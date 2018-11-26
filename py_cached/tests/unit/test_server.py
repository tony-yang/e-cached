import unittest

from py_cached.core.cache import Cache
from py_cached.core.server import CacheServer

import py_cached.settings_tests
import logging
logger = logging.getLogger(__name__)

class TestCacheServer(unittest.TestCase):
    def setUp(self):
        self.cs = CacheServer(exit=True)
        self.cache = Cache()

    def tearDown(self):
        self.cs.shutdown_server()

    def test_serve_set_command(self):
        command = 'SET a b'
        output = self.cs.serve_request(command, self.cache)
        expected = None
        self.assertEqual(output, expected, 'Wrong output when set a key value pair to the cache')
        self.assertEqual(self.cache.get('a'), 'b', 'Wrong value set for the key')

    def test_serve_wrong_set_command_with_exception(self):
        command = 'SET a b c'
        with self.assertRaises(Exception, msg='Incorrect number of argument. SET expects a key value pair but too many arguments were given'):
            output = self.cs.serve_request(command, self.cache)

    def test_serve_wrong_set_command2_with_exception(self):
        command = 'SET a'
        with self.assertRaises(Exception, msg='Incorrect number of argument. SET expects a key value pair but only key was given'):
            output = self.cs.serve_request(command, self.cache)

    def test_serve_get_command_none_exists(self):
        command = 'GET none'
        output = self.cs.serve_request(command, self.cache)
        expected = None
        self.assertEqual(output, expected, 'Wrong output when getting a nonexist key from the cache')

    def test_serve_get_command_exists(self):
        command = 'SET a b'
        self.cs.serve_request(command, self.cache)

        command = 'GET a'
        output = self.cs.serve_request(command, self.cache)
        expected = 'b'
        self.assertEqual(output, expected, 'Wrong output when getting an exist key from the cache')

    def test_serve_wrong_get_command_with_exception(self):
        command = 'GET d e'
        with self.assertRaises(Exception, msg='Incorrect number of argument. GET expects a key only'):
            output = self.cs.serve_request(command, self.cache)
