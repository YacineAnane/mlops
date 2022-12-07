import time
import pandas as pd
import numpy as np
import streamlit as st
from kafka import KafkaConsumer
import json

# Init consumer
topic = "view-count_predictions"
consumer = KafkaConsumer(
        topic,
        value_deserializer = lambda x: json.loads(x.decode("utf-8")),
        bootstrap_servers="localhost:9092")

# Page configuration
st.set_page_config(
    layout="centered", page_icon="📺", page_title="View count predictions"
)
st.title("Youtube videos' view count predictions")
st.write(
    """This app displays youtube vidos' view count predictions from  therr average popularity score (like rate of the other videos of the channel), number of subscribers of the channel, total number of videos and views of the channel, and the duration of the video."""
)

# Create table
table_df = pd.DataFrame([[0.,0.,0.,0.,0.,0.]], columns=["Average polarity score", "Subscribers", "Total videos", "Total views", "Duration (s)", "View count predictions"])
table = st.table(table_df)

# Add row to table for each consumed prediction
for msg in consumer:
    predictions = pd.DataFrame(msg.value["predictions"])
    predictions = predictions.astype(float)
    table.add_rows(predictions)