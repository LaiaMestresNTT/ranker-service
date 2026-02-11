from confluent_kafka import Consumer, KafkaError, KafkaException

# Configuración del consumidor
conf = {
    'bootstrap.servers': 'localhost:9092',  # Dirección del servidor Kafka
    'group.id': 'confirmation-group',  # ID del grupo para gestionar el offset
    'auto.offset.reset': 'earliest'  # Lee desde el principio si no hay offset previo
}

consumer = Consumer(conf)

TOPIC = "scraping_finished"


def consumir_mensajes():
    try:
        # Suscribirse al tópico
        consumer.subscribe([TOPIC])
        print(f"Escuchando el tópico: {TOPIC}...")

        while True:
            # Espera un mensaje (timeout de 1.0 segundo)
            msg = consumer.poll(timeout=1.0)

            if msg is None:
                continue

            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    # Fin de la partición (opcional manejarlo)
                    continue
                else:
                    raise KafkaException(msg.error())

            # Imprimir el mensaje recibido
            print(f"Mensaje recibido: {msg.value().decode('utf-8')} en la clave {msg.key()}")

    except KeyboardInterrupt:
        print("Deteniendo el consumidor...")
    finally:
        # Cerrar el consumidor de forma limpia para confirmar los offsets
        consumer.close()


consumir_mensajes()