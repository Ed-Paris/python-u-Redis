import redis
from time import sleep


r = redis.Redis(host = 'localhost', port=6379)

r.hset('w', 'id', '1')
r.hset('w', 'palabra', 'Que Xopa')
r.hset('w', 'significado', 'Saludar')

print(r.hgetall('w'))
sleep(1)

r.hset('w', 'id', '2')
r.hset('w', 'palabra', 'Chantin')
r.hset('w', 'significado', 'Casa')

print(r.hgetall('w'))
sleep(1)

r.hset('w', 'id', '3')
r.hset('w', 'palabra', 'Nave')
r.hset('w', 'significado', 'Carro')

print(r.hgetall('w'))
sleep(1)

r.hset('w', 'id', '4')
r.hset('w', 'palabra', 'Parking')
r.hset('w', 'significado', 'Fiesta')

print(r.hgetall('w'))
sleep(1)

r.hset('w', 'id', '5')
r.hset('w', 'palabra', 'Fren')
r.hset('w', 'significado', 'Amigo')

print(r.hgetall('w'))
sleep(1)

#hexists('palabra','valor que desea saber si existe en la tabla')
#if r.hexists('palabra','bro') == True:
#    print("Existe la palabra en el listado")
#print("La palabra no existe")
