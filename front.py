import time
import pandas as pd
import numpy as np
import streamlit as st
from kafka import KafkaConsumer
import json

topic = "view-count_predictions"
# Init consumer
consumer = KafkaConsumer(
        topic,
        value_deserializer = lambda x: json.loads(x.decode("utf-8")),
        bootstrap_servers="localhost:9092")

# Create table
table_df = pd.DataFrame([[0.,0.,0.,0.,0.,0.]], columns=["Average polarity score", "Subscribers", "Total videos", "Total views", "Duration (s)", "View count predictions"])
table = st.table(table_df)

# Add row to table for each consumed prediction
for msg in consumer:
    predictions = pd.DataFrame(msg.value["predictions"])
    predictions = predictions.astype(float)
    table.add_rows(predictions)