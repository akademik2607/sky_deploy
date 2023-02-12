
import redis

r = redis.Redis(host='redis')



while True:
    try:
        val = input('Введите пример: ')
    except EOFError:
        val = 'stop'
    if val.lower() == 'stop':
        r.publish('operations', val)
        break
    r.publish('operations', val)
print("Вы завершили программу")
