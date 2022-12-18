import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
import joblib
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

#preprocessing
dataset = pd.concat([pd.read_csv("../data/ytunlabeled2.csv"), pd.read_csv("../data/ytunlabeled3.csv")])
dataset = dataset[["viewCount", "avg polarity score", "subscribers", "totalVideos", "totalViews", "duration"]]
dataset = dataset[dataset["avg polarity score"].notna()]
label = "viewCount"

def convert_timestamp(time):
    parsing_str = "PT"

    if "H" in time:
        parsing_str += "%HH"
    if "M" in time:
        parsing_str += "%MM"
    if "S" in time:
        parsing_str += "%SS"

    t = datetime.strptime(time, parsing_str)
    # convert to timedelta to get the total seconds
    td = timedelta(minutes=t.minute, seconds=t.second)
    return td.total_seconds()

dataset["duration"] = dataset["duration"].apply(lambda time: convert_timestamp(time))
x_train, x_test, y_train, y_test = train_test_split(dataset.drop(columns=[label]), dataset[label], test_size=0.33, random_state=42)

#model
model = RandomForestRegressor()
model.fit(x_train, y_train)

preds = model.predict(x_test)

# save the model to disk
filename = 'model.joblib'
joblib.dump(model, filename)
