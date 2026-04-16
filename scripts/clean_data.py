import pandas as pd
from pathlib import Path

# Paths
base_path = Path(__file__).resolve().parent.parent
input_file = base_path / "data" / "student-scores.csv"
output_file = base_path / "data" / "cleaned_students.csv"

# Load data
df = pd.read_csv(input_file)

# Clean column names
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# Remove duplicate rows
df = df.drop_duplicates()

# Drop rows with missing values
df = df.dropna()

# Create average score column if subject columns exist
possible_cols = [
    "math_score",
    "history_score",
    "physics_score",
    "chemistry_score",
    "biology_score",
    "english_score"
]

if all(col in df.columns for col in possible_cols):
    df["average_score"] = df[possible_cols].mean(axis=1)
if all(col in df.columns for col in possible_cols):
    df["average_score"] = df[possible_cols].mean(axis=1)

# Save cleaned data
df.to_csv(output_file, index=False)

print("Data cleaned successfully!")
print(f"Cleaned file saved to: {output_file}")
print(df.head())