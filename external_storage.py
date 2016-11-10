import config
import redis

class ExternalStorage:
    def __init__(self):
        self.redis_instance = redis.StrictRedis(host=config.REDIS['host'],
                                                port=config.REDIS['port'],
                                                db=config.REDIS['db'])

    def set(self, key, value):
        self.redis_instance.set(key, value)

    def get(self, key):
        return self.redis_instance.get(key)

    def exists(self, key):
        return self.redis_instance.exists(key)
