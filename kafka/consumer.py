from kafka import KafkaConsumer
import numpy as np
import pandas as pd
import json
import joblib

print("Loading model")
loaded_model = joblib.load("model/random_forest.joblib")
prod_data = []

topic = "view-count_producer"
consumer = KafkaConsumer(
        topic,
        value_deserializer = lambda x: json.loads(x.decode("utf-8")),
        bootstrap_servers="localhost:9092")

print("Start consumming")
for msg in consumer:
    data = np.array(msg.value["X"])

    if data.shape[-1] != 5:
        print("Data shape is incorrect. Expected 5, Got", data.shape)
        continue

    print("Predictions:", np.array(loaded_model.predict(data)))
    prod_data.append(data)
    pd.DataFrame(prod_data).to_csv("data/prod_data.csv", mode='a', index=False, header=False)
