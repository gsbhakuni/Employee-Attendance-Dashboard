import pandas as pd

def load_data(uploaded_file):
    df = pd.read_csv(uploaded_file)
    df["date"] = pd.to_datetime(df["date"]).dt.date
    return df

def summary(df):
    department_summary = (
        df.groupby("department")["status"].value_counts().unstack(fill_value=0)
    )
    department_summary["Attendance%"] = (
        100
        * (department_summary["Present"] + department_summary["Work From Home"])
        / (
            department_summary["Present"]
            + department_summary["Work From Home"]
            + department_summary["Absent"]
            + department_summary["Leave"]
        )
    ).round(2)
    return department_summary