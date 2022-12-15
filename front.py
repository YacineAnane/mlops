import pandas as pd
import streamlit as st
from kafka import KafkaConsumer, KafkaProducer
import asyncio
import json

# Init consumer
pred_topic = "view-count_predictions"
consumer = KafkaConsumer(
        pred_topic,
        value_deserializer = lambda x: json.loads(x.decode("utf-8")),
        # enable_auto_commit=False,
        auto_offset_reset = "earliest",
        bootstrap_servers="localhost:9092")

# Init producer
data_topic = "youtube_data"
producer = KafkaProducer(
        value_serializer=lambda x: json.dumps(x).encode("utf-8"),
        bootstrap_servers="localhost:9092")

def send_data(X, data_topic, producer):
        message = {"X": X}
        print(message)
        print("\n\nSendind message:", message)
        producer.send(data_topic, message)
        producer.flush()

# def main():
# Page configuration
st.set_page_config(
    layout="centered", page_icon="📺", page_title="View count predictions"
)
st.title("Youtube videos' view count predictions")
st.write(
    """This app displays youtube videos view count predictions from their average popularity score (like rate of the other videos of the channel), number of subscribers of the channel, the total number of videos and views of the channel, and the duration of the video."""
)

# Take input from user
st.write("Make a prediction:")

csv = st.file_uploader("Upload a csv containning the data.")
if csv is not None:
    dataframe = pd.read_csv(csv)

if st.button("Make prediction"):
    print("Send data")
    send_data([list(x) for x in dataframe.values], data_topic, producer)
    msg_pack = consumer.poll(timeout_ms=1000)
    msg = list(msg_pack.values())[-1][-1].value

    predictions = pd.DataFrame(msg["predictions"])
    predictions = predictions.astype(float)
    predictions.columns = ["Average polarity score", "Subscribers", "Total videos", "Total views", "Duration (s)", "View count predictions"]
    table = st.table(predictions)