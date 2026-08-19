# Employee Attendance Analytics & Prediction Dashboard

A Streamlit-based data analytics and machine learning application that helps organizations monitor employee attendance, generate workforce insights, and predict future attendance status using historical attendance records.

## Overview

Managing employee attendance is essential for workforce planning, productivity tracking, and HR decision-making. This project provides an interactive dashboard that allows users to upload attendance data, explore key attendance metrics, visualize attendance trends, analyze department-wise and employee-wise performance, and predict future attendance behavior using a machine learning model.

The application combines data analytics and predictive modeling into a single, user-friendly interface.

---

## Features

### Attendance Analytics

* Total employee count
* Present employee count
* Work From Home (WFH) count
* Absent employee count
* Leave count
* Overall attendance percentage

The dashboard calculates attendance KPIs directly from the uploaded dataset. Attendance percentage is computed using both Present and Work From Home records.

### Interactive Visualizations

* Attendance status distribution
* Department-wise attendance analysis
* Employee-wise attendance summary
* Daily attendance trends

The dashboard generates visual insights that help HR teams quickly identify attendance patterns and workforce behavior.

### Department-Level Insights

Analyze attendance performance across departments with:

* Department-wise employee distribution
* Attendance percentages by department
* Comparative attendance analysis

Attendance metrics are calculated using Present, Work From Home, Absent, and Leave records.

### Employee-Level Analysis

View attendance summaries for individual employees, including attendance percentages and attendance status breakdowns.

### Machine Learning Attendance Prediction

The dashboard includes a predictive module that uses a Random Forest Classifier to forecast an employee's next attendance status based on their three previous attendance records. Supported prediction classes include:

* Present
* Absent
* Work From Home
* Leave

The model trains dynamically from the uploaded dataset and predicts future attendance behavior.

---

## Tech Stack

### Frontend

* Streamlit

### Data Processing

* Pandas
* NumPy

### Data Visualization

* Matplotlib

### Machine Learning

* Scikit-learn
* Random Forest Classifier

---

## Project Structure

```text
Employee-Attendance-Dashboard/
│
├── app.py                # Streamlit application
├── analytics.py          # KPI and attendance metrics
├── prediction.py         # Machine learning pipeline
├── util.py               # Data loading and summaries
├── dataset.csv           # Attendance dataset
├── requirements.txt
└── README.md
```

---

## How It Works

### Step 1: Upload Attendance Dataset

The application accepts attendance data in CSV format and automatically loads and preprocesses date fields.

### Step 2: Generate Analytics

The dashboard computes:

* Employee count
* Attendance percentage
* Present records
* WFH records
* Leave records
* Absent records

and displays them as KPI cards.

### Step 3: Explore Visual Insights

Users can interact with:

* Attendance distribution charts
* Department summaries
* Daily attendance reports
* Employee attendance reports

### Step 4: Predict Future Attendance

The machine learning model creates training samples using the previous three attendance records of an employee and predicts the next attendance status.

---

## Expected Dataset Format

Your CSV file should contain fields similar to:

| Column      | Description                               |
| ----------- | ----------------------------------------- |
| employee_id | Unique employee identifier                |
| date        | Attendance date                           |
| status      | Present, Absent, Work From Home, or Leave |
| department  | Employee department                       |

---

## Installation

### Clone Repository

```bash
git clone https://github.com/gsbhakuni/Employee-Attendance-Dashboard.git
cd Employee-Attendance-Dashboard
```

### Create Virtual Environment

```bash
python -m venv venv
```

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run app.py
```

The application will launch in your browser.

---

## Machine Learning Approach

The prediction module transforms attendance statuses into numerical values:

| Status         | Encoding |
| -------------- | -------- |
| Absent         | 0        |
| Present        | 1        |
| Work From Home | 2        |
| Leave          | 3        |

## A Random Forest classifier is trained using sequences of three previous attendance records to predict the next attendance status.

## Business Value

This solution helps organizations:

* Monitor workforce attendance efficiently
* Identify absenteeism trends
* Evaluate departmental attendance performance
* Track work-from-home adoption
* Support HR decision-making through analytics
* Predict future attendance patterns

---

## Future Enhancements

* Employee attendance forecasting using time-series models
* Downloadable reports (PDF/Excel)
* Role-based authentication
* Real-time database integration
* Interactive Plotly visualizations
* Attendance anomaly detection
* Employee performance correlation analysis
* Cloud deployment (AWS/Azure/GCP)

---

## Author

**Gaurav Singh Bhakuni**

GitHub: https://github.com/gsbhakuni

---

## License

This project is open-source and available under the MIT License.
