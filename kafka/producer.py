from kafka import KafkaProducer
import json

topic = "view-count_producer"
producer = KafkaProducer(
        value_serializer=lambda x: json.dumps(x).encode("utf-8"),
        bootstrap_servers="localhost:9092")


message = {"X": [[0,0,0,0,0]]}

producer.send(topic, message)
producer.flush()
