 Student Data Analytics Pipeline & Dashboard

Project Overview

This project demonstrates an end-to-end **data analytics workflow**, beginning with raw educational data from Kaggle and progressing through **data cleaning, transformation, modelling, and visualization** using **Python** and **Power BI**.

The objective of this project was to analyze student academic performance, study habits, and career aspirations while developing hands-on experience in **data engineering, relational modelling, and business intelligence**.

---

 Project Workflow

### 1. Data Collection (Kaggle Dataset)

The project began with downloading a student performance dataset from **Kaggle** containing student demographics, academic scores, study habits, and career aspirations.

The raw dataset included variables such as:

* Academic subject scores
* Weekly self-study hours
* Career aspirations
* Absence days
* Gender
* Extracurricular activities

---

### 2. Data Cleaning & Preparation (Python + VS Code)

Using **Python in Visual Studio Code**, the raw dataset was cleaned and transformed to improve usability for analytics.

### Cleaning tasks performed:

 Standardized column names
Removed duplicates
 Removed missing/null values
Created a new calculated field:

* `average_score`

### Technologies Used:

* Python
* Pandas
* VS Code

Example transformation:

```python
df["average_score"] = (
    df["math_score"] +
    df["physics_score"] +
    df["chemistry_score"] +
    df["biology_score"] +
    df["english_score"] +
    df["history_score"]
) / 6
```

The cleaned dataset was exported as:

```text
cleaned_students.csv
```

---

### 3. Data Visualization (Power BI)

The cleaned dataset was imported into **Power BI Desktop** to create interactive visualizations and uncover insights from student behavior and academic performance.

### Visualizations created:

#### Study Hours vs Student Performance

A scatter plot was used to analyze the relationship between:

* Weekly self-study hours
* Student average scores

**Insight:**
Students who studied more hours generally achieved higher academic performance, although some outliers suggested additional influencing factors.

---

#### 🥧 Student Career Aspiration Distribution

A pie chart was created to visualize:

* Percentage of students choosing each career aspiration

This provided insights into the popularity of different career paths among students.

---

#### Average Student Performance Analysis

Charts were created to compare:

* Academic performance across subjects
* Student performance trends

---

## Data Modelling (Power BI Model View)

To improve data organization and simulate a **relational database structure**, the original dataset was broken into **three related tables**.

### Tables Created

### 1. Student_Profile

Contains student demographic and personal information:

* `id`
* `gender`
* `career_aspiration`
* `part_time_job`
* `extracurricular_activities`
* `first_name`
* `last_name`

---

### 2. Student_Academics

Contains academic performance data:

* `id`
* `math_score`
* `physics_score`
* `chemistry_score`
* `biology_score`
* `english_score`
* `history_score`
* `average_score`

---

### 3. Study_Habits

Contains student behavioral metrics:

* `id`
* `weekly_self_study_hours`
* `absence_days`

---

## 🔗 Relationships & Database Modelling

A **primary key (`id`)** was used to create relationships between the tables.

### Relationship Type:

 **One-to-One (1:1)**

Relationships created:

```text
Student_Profile.id ↔ Student_Academics.id
Student_Profile.id ↔ Study_Habits.id
```

This relational model improved:

* Data organization
* Query efficiency
* Scalability
* Model readability

---

## 🛠️ Tools & Technologies

| Technology | Purpose                           |
| ---------- | --------------------------------- |
| Python     | Data cleaning & transformation    |
| Pandas     | Data manipulation                 |
| VS Code    | Development environment           |
| Power BI   | Data visualization & dashboarding |
| Kaggle     | Dataset source                    |
| GitHub     | Project version control           |

---

## Project Structure

```text
student-data-pipeline/
│── data/
│   ├── student-scores.csv
│   ├── cleaned_students.csv
│
│── scripts/
│   ├── clean_data.py
│
│── output/
│   ├── dashboard.png
│   ├── student_dashboard.pbix
│
│── README.md
```

---

## Key Skills Demonstrated

* Data Cleaning
* Data Transformation
* Python Programming
* Exploratory Data Analysis (EDA)
* Data Visualization
* Power BI Dashboarding
* Relational Data Modelling
* One-to-One Table Relationships
* Problem Solving
* Data Storytelling

---

## Future Improvements

Potential future enhancements include:

* Adding predictive analytics
* Building machine learning models
* Automating the ETL process
* Publishing an interactive dashboard online

---

## Author

**KC Amaefule**

🌐 Personal Website: https://kcmaths.online/
💻 GitHub: https://github.com/AmaefuleMcDonald
# student-data-pipeline
Student Data cleaner
