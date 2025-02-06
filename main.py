import redis
 
# Conectamos a Redis

try:

    r = redis.Redis(host='186.6.3.120', port=6379, db=0, decode_responses=True)

except redis.ConnectionError as e:

    print(f"Error de conexión a Redis: {e}")

    exit(1)
 
def subscribe():

    try:

        # Creamos una suscripción

        pubsub = r.pubsub()

        pubsub.subscribe('joerlyn')

        print("Esperando mensajes en el canal 'joerlyn'...")
 
        # Iteramos sobre los mensajes recibidos

        for message in pubsub.listen():

            if message['type'] == 'message':  # Filtramos solo los mensajes

                print(f"Nuevo mensaje recibido: {message['data']}")
 
    except Exception as e:

        print(f"Error en la suscripción: {e}")
 
# Ejecutamos la suscripción

subscribe()

 