import pandas as pd

def load_data(uploaded_file):
    df = pd.read_csv(uploaded_file)
    df["date"] = pd.to_datetime(df["date"]).dt.date
    return df

def dep_summary(df):
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

def emp_summary(df):
    employee_summary = (
        df.groupby("employee_id")["status"].value_counts().unstack(fill_value=0)
    )
    employee_summary["Attendance%"] = (
            100
            * (employee_summary["Present"] + employee_summary["Work From Home"])
            / (
                employee_summary["Present"]
                + employee_summary["Work From Home"]
                + employee_summary["Absent"]
                + employee_summary["Leave"]
            )
        ).round(2)
    return employee_summary
