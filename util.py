import pandas as pd

def load_data(uploaded_file):
    df = pd.read_csv(uploaded_file)
    df["date"] = pd.to_datetime(df["date"]).dt.date
    return df