import numpy as np
from sklearn.ensemble import RandomForestClassifier


status_mapping = {
    "Absent": 0,
    "Present": 1,
    "Work From Home": 2,
    "Leave": 3
}

reverse_mapping = {
    0: "Absent",
    1: "Present",
    2: "Work From Home",
    3: "Leave"
}


def prepare_training_data(df):
    X = []
    y = []

    employee_ids = df["employee_id"].unique()

    for emp in employee_ids:
        emp_data = df[df["employee_id"] == emp].sort_values("date")

        attendance_values = (
            emp_data["status"]
            .map(status_mapping)
            .tolist()
        )

        if len(attendance_values) >= 4:
            for i in range(len(attendance_values) - 3):
                X.append(attendance_values[i:i+3])
                y.append(attendance_values[i+3])

    return np.array(X), np.array(y)


def train_model(X, y):
    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )

    model.fit(X, y)
    return model


def predict_attendance(model, s1, s2, s3):
    sample = np.array([
        [
            status_mapping[s1],
            status_mapping[s2],
            status_mapping[s3]
        ]
    ])

    prediction = model.predict(sample)[0]

    return reverse_mapping[prediction]