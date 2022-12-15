from kafka import KafkaProducer
import pandas as pd
import json
import sys

if len(sys.argv) != 2 or not sys.argv[1].endswith(".csv"):
    print("Usage:")
    print("python producer.py <csv file>")
    exit()

data = pd.read_csv(sys.argv[1])

topic = "youtube_data"
producer = KafkaProducer(
        value_serializer=lambda x: json.dumps(x).encode("utf-8"),
        bootstrap_servers="localhost:9092")

data = [list(x) for x in data.values]
message = {"X": data}

producer.send(topic, message)
producer.flush()
