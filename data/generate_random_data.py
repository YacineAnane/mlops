import pandas as pd
import numpy as np
import sys

if len(sys.argv) != 2:
    print("Usage:")
    print("python generate_random_data.py <Number of observations>")
    exit()

size = int(sys.argv[1])

dataframe = pd.read_csv("data/train.csv").iloc[:, -5:]
dataframe_summary = dataframe.describe()
random_data = [pd.Series(np.random.normal(dataframe_summary.loc["mean", col], dataframe_summary.loc["std", col], size)) for col in dataframe.columns]
concat = pd.concat(random_data, axis=1)
concat.columns = dataframe.columns
for col in ["subscribers", "totalVideos", "totalViews"]:
    concat[col] = concat[col].apply(lambda x: int(x))

concat.to_csv("data/random_data.csv", index=False)

