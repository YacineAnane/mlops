import pandas as pd
import numpy as np
from eurybia import SmartDrift
from os import listdir
from os.path import isfile, join
import sys


def check_data_drift(df_current, df_baseline, output_file="report.html", title="Data drift report"):
  sd = SmartDrift(
    df_current=df_current,
    df_baseline=df_baseline,
    # deployed_model=model, # Optional: put in perspective result with importance on deployed model
    dataset_names={"df_current": "Production dataset", "df_baseline": "Trainning dataset"} # Optional: Names for outputs
    )

  sd.compile()

  sd.generate_report(
    output_file=output_file,
    title_story=title
    )

if len(sys.argv) < 3:
    print("Usage: python data_drift.py <path to production data folder> <path to trainning data folder>") 
    exit

production_data = pd.read_csv(sys.argv[1])
training_data = pd.read_csv(sys.argv[2])

check_data_drift(production_data, training_data)
