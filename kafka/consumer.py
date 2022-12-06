from kafka import KafkaConsumer
import numpy as np
import json

topic = "view-count_producer"
consumer = KafkaConsumer(
        topic,
        value_deserializer = lambda x: json.loads(x.decode("utf-8")),
        bootstrap_servers="localhost:9092")

for msg in consumer:
    data = msg.value["X"]
    print(np.array(data).flatten())
