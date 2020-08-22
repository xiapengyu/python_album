import redis


def init_client():
    client = redis.StrictRedis(host='192.168.204.128', port=6379, db=0)
    return client


def set_key(key, value):
    client = init_client()
    client.set(key, value)


def set_key_expire(key, value, time):
    client = init_client()
    client.set(key, value, time)


def get_key(key):
    client = init_client()
    result = client.get(key)
    return result


if __name__ == "__main__":
    set_key("foo1", "far")
    set_key("foo2", "far")
    set_key("foo3", "far")
