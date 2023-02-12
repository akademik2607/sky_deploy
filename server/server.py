import redis
import time

r = redis.Redis(host='redis')

p = r.pubsub()

p.subscribe('operations')

p.get_message()

while True:
    message = p.get_message()
    if message and message['data'] != 1:
        if message['data'].lower() == 'stop':
            break
        print(f'{message["data"]} = {eval(message["data"])}')
    time.sleep(0.1)
print('server is stoped!')
