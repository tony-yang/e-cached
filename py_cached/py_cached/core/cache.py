import logging, py_cached.settings
logger = logging.getLogger(__name__)

class Cache:
    def __init__(self):
        logger.info('Create a Cache object')
        self.cache = {}

    def set(self, k, v):
        self.cache[k] = v

    def get(self, k):
        if k in self.cache:
            value = self.cache[k]
        else:
            value = None
        return value
