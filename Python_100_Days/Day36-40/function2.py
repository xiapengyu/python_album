import redis


def set_key(key, value):
    client = redis.Redis(host='127.0.0.1', port=6379)
    client.set(key, value)


def get_key(key):
    client = redis.Redis(host='127.0.0.1', port=6379)
    value = client.get(key)
    print(value.decode('utf-8'))


def operate():
    client = redis.Redis(host='127.0.0.1', port=6379)
    client.set('na', 'Lucy')
    results = client.keys('na*')
    for item in results:
        print(item.decode('utf-8'))


def main():
    set_key('name', 'Lily')
    get_key('name')
    operate()


if __name__ == '__main__':
    main()
