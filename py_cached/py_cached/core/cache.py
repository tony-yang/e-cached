import logging, py_cached.settings
logger = logging.getLogger(__name__)

class Cache:
    def __init__(self):
        logger.info('Create a Cache object')
