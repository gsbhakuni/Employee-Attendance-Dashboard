import streamlit as st
import matplotlib.pyplot as plt
import util
import analytics
import prediction
from sklearn.model_selection import train_test_split
st.set_page_config(page_title="Employee Attendance Dashboard", layout="wide")

st.title("Employee Attendance Analytics and Prediction Dashboard")

st.write(
    "Upload the attendance dataset to view analytics and predict employee attendance."
)

uploaded_file = st.file_uploader("Upload Attendance CSV File", type=["csv"])

if uploaded_file is not None:
    df = util.load_data(uploaded_file)

    st.subheader("Dataset Preview")
    st.dataframe(df.head(5))

    (
        total_employees,
        present_count,
        wfh_count,
        absent_count,
        leave_count,
        attendance_percentage,
    ) = analytics.get_metrics(df)

    col1, col2, col3, col4, col5, col6 = st.columns(6)

    col1.metric("Employees", total_employees)
    col2.metric("Present", present_count)
    col3.metric("WFH", wfh_count)
    col4.metric("Absent", absent_count)
    col5.metric("Leave", leave_count)
    col6.metric("Attendance %", f"{attendance_percentage}%")

    st.subheader("Attendance Status Distribution")

    status_counts = df["status"].value_counts()

    fig, ax = plt.subplots()

    ax.bar(status_counts.index, status_counts.values)

    ax.set_xlabel("Status")
    ax.set_ylabel("Count")
    ax.set_title("Attendance Distribution")

    plt.xticks(rotation=20)

    st.pyplot(fig)

    if "department" in df.columns:
        st.subheader("Department-wise Attendance Summary")
        department_summary = util.dep_summary(df)
        st.dataframe(department_summary)

        st.subheader("Department Distribution")

        fig2, ax2 = plt.subplots()

        department_summary.plot(kind="bar", ax=ax2)

        ax2.set_xlabel("Department")
        ax2.set_ylabel("No. of Employees")
        ax2.set_title("Department-wise Status")
        plt.xlabel("Departments")
        plt.ylabel("No. of Employees")

        plt.xticks(rotation=45)

        st.pyplot(fig2)

    st.subheader("Employee-wise Attendance Summary")
    employee_summary = util.emp_summary(df)
    st.dataframe(employee_summary)

    st.subheader("Daily Attendance Trend")

    daily_attendance = df.groupby("date")["status"].apply(
        lambda x: ((x == "Present") | (x == "Work From Home")).sum()
    )

    st.dataframe(daily_attendance)

    X, y = prediction.prepare_training_data(df)

    if len(X) > 20:
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        model = prediction.train_model(X_train, y_train)
        
        options = ["Present", "Absent", "Work From Home", "Leave"]
        s1 = st.selectbox("Status 3 Records Ago", options)
        s2 = st.selectbox("Status 2 Records Ago", options)
        s3 = st.selectbox("Previous Status", options)

        if st.button("Predict"):
            result = prediction.predict_attendance(model, s1, s2, s3)
            st.success(f"Predicted Status: {result}")
    else:
        st.warning("Not enough data available for model training.")

else:
    st.info("Upload the attendance CSV file to begin.")