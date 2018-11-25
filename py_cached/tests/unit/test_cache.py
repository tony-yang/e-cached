import unittest

from py_cached.core.cache import Cache

import py_cached.settings_tests
import logging
logger = logging.getLogger(__name__)

class TestCache(unittest.TestCase):
    def setUp(self):
        self.c = Cache()

    def test_set_get_key(self):
        self.c.set('test-key', 15)
        output = self.c.get('test-key')
        expected = 15
        self.assertEqual(output, expected, 'ERROR: calling get on the key returns incorrect value')
