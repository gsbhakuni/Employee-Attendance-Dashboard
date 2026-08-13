def get_metrics(df):
    total_employees = df["employee_id"].nunique()

    present_count = (df["status"] == "Present").sum()

    wfh_count = (df["status"] == "Work From Home").sum()

    absent_count = (df["status"] == "Absent").sum()

    leave_count = (df["status"] == "Leave").sum()

    attendance_percentage = round(((present_count + wfh_count) / len(df)) * 100, 2)

    return total_employees, present_count, wfh_count, absent_count, leave_count, attendance_percentage

 