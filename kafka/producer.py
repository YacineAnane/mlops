from kafka import KafkaProducer
import pandas as pd
import json
import sys

if len(sys.argv) != 2 or not sys.argv[1].endswith(".csv"):
    print("Usage:")
    print("python producer.py <csv file>")
    exit()

data = pd.read_csv(sys.argv[1])

topic = "view-count_producer"
producer = KafkaProducer(
        value_serializer=lambda x: json.dumps(x).encode("utf-8"),
        bootstrap_servers="localhost:9092")


message = {"X": [list(x) for x in data.values]}

producer.send(topic, message)
producer.flush()
