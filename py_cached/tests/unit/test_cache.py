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

    def test_get_non_key_value_gracefully_fail(self):
        output = self.c.get('non-exist')
        expected = None
        self.assertEqual(output, expected, 'ERROR: get non existing key should return none and not raise exception')
