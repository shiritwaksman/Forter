import config
import redis

class ExternalStorage:
    def __init__(self):
        """Open connection to redis"""
        self.redis_instance = redis.StrictRedis(host=config.REDIS['host'],
                                                port=config.REDIS['port'],
                                                db=config.REDIS['db'])

    def set(self, key, value):
        """Insert (key, value) into redis"""
        self.redis_instance.set(key, value)

    def get(self, key):
        """Get value by key"""
        return self.redis_instance.get(key)

    def exists(self, key):
        """Return true if key exist in redis"""
        return self.redis_instance.exists(key)
