import time

from main import redis, Product

key = 'order_completed'
group = 'inventory-group'

try:
    redis.xgroup_create(key, group)
except:
    print("Group already exists!")


while True:
    try:
        results = redis.xreadgroup(group, key, {key: '>'}, None)
    except Exception as e:
        print(str(e))
    time.sleep(1)