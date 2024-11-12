import redis
import json


class UserRedisStorage:
    def __init__(self, host='localhost', port=6379, db=0):
        self.r = redis.Redis(host=host, port=port, db=db)

    def set_data(self, user_id, key, value, expiration=None):
        user_key = f"user:{user_id}"
        self.r.hset(user_key, key, json.dumps(value))
        if expiration is not None:
            self.r.expire(user_key, expiration)

    def get_data(self, user_id, key, pop=False):
        user_key = f"user:{user_id}"
        data = self.r.hget(user_key, key)
        if pop and data is not None:
            self.r.hdel(user_key, key)
        return json.loads(data) if data else None

    def get_all_data(self, user_id):
        user_key = f"user:{user_id}"
        data = self.r.hgetall(user_key)
        decoded_data = {key.decode(): json.loads(value) for key, value in data.items()}
        return decoded_data

    def delete_data(self, user_id, key):
        user_key = f"user:{user_id}"
        self.r.hdel(user_key, key)

    def delete_all_data(self, user_id):
        user_key = f"user:{user_id}"
        self.r.delete(user_key)

    def pop_data(self, user_id, key):
        return self.get_data(user_id, key, pop=True)
