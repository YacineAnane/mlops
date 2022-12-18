from kafka import KafkaConsumer, KafkaProducer
import numpy as np
import pandas as pd
import json
import joblib

# Loading model
loaded_model = joblib.load("deployement/model.joblib")

# Init topics
consumed_topic = "youtube_data"
produced_topic = "view-count_predictions"

# Init consumer
consumer = KafkaConsumer(
        consumed_topic,
        value_deserializer = lambda x: json.loads(x.decode("utf-8")),
        bootstrap_servers="localhost:9092")

# Init producer
producer = KafkaProducer(
        value_serializer=lambda x: json.dumps(x).encode("utf-8"),
        bootstrap_servers="localhost:9092")

prod_data = []
for msg in consumer:
    data = np.array(msg.value["X"])

    if data.shape[-1] != 5:
        print("Data shape is incorrect. Expected 5, Got", data.shape)
        continue

    predictions = loaded_model.predict(data)
    print("Predictions:", predictions)
    
    # Save youtube data
    prod_data.append(data)
    pd.DataFrame(prod_data[0]).to_csv("data/prod_data.csv", mode='a', index=False, header=False)

    # Send prediction to streamlit with kafka
    pred_df = pd.concat([pd.DataFrame(data), pd.Series(predictions)], axis=1)
    message = {"predictions": [list(line) for line in pred_df.values]}

    producer.send(produced_topic, message)
    producer.flush()
