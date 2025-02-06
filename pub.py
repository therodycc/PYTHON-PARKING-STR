import redis
 
CHANNEL ='joerlyn'
usuario=input('Ingrese su Usuario: ')
 
client=redis.StrictRedis(host='186.6.3.120',port=6379,db=0)
 
while True:
    message= input('Ingrese el mensaje: ')
    client.publish(CHANNEL,f'{usuario}: {message}')