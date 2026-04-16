import sqlite3
import pandas as pd

conn = sqlite3.connect("../data/students.db")

df = pd.read_csv("../data/cleaned_students.csv")

df.to_sql("students", conn, if_exists="replace", index=False)

conn.close()

print("Data stored in database!")