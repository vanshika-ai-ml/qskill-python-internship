import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv("Student-Performance-Analysis/StudentsPerformance.csv")

print("Dataset Loaded Successfully!")
print(data.head())
print("\nDataset Shape:", data.shape)

print("\nMissing Values:")
print(data.isnull().sum())

print("\nDataset Information:")
print(data.info())

print("\nAverage Scores:")
print("Math Score:", round(data["math score"].mean(), 2))
print("Reading Score:", round(data["reading score"].mean(), 2))
print("Writing Score:", round(data["writing score"].mean(), 2))

print("\nHighest Math Score:", data["math score"].max())
print("Lowest Math Score:", data["math score"].min())

# Math Score Distribution
plt.figure(figsize=(8,5))
plt.hist(data["math score"], bins=10, edgecolor="black")
plt.title("Distribution of Math Scores")
plt.xlabel("Math Score")
plt.ylabel("Number of Students")
plt.savefig("Student-Performance-Analysis/images/math-score-distribution.png")
plt.show()

# Average Scores Bar Chart
average_scores = [
    data["math score"].mean(),
    data["reading score"].mean(),
    data["writing score"].mean()
]

subjects = ["Math", "Reading", "Writing"]

plt.figure(figsize=(6,5))
plt.bar(subjects, average_scores)

plt.title("Average Scores")
plt.xlabel("Subjects")
plt.ylabel("Average Score")

plt.savefig("Student-Performance-Analysis/images/average-scores.png")

plt.show()

# Reading vs Writing Scatter Plot

plt.figure(figsize=(8,6))

plt.scatter(
    data["reading score"],
    data["writing score"],
    alpha=0.7,
    color="green"
)

plt.title("Reading Score vs Writing Score")
plt.xlabel("Reading Score")
plt.ylabel("Writing Score")

plt.savefig("Student-Performance-Analysis/images/reading-vs-writing.png")

plt.show()

# gender-wise average math score 

gender_math = data.groupby("gender")["math score"].mean()

plt.figure(figsize =(6,5))
gender_math.plot(kind ="bar")
plt.title("Average Math Score by Gender")
plt.xlabel("Gender")
plt.ylabel("Average Math Score")

plt.savefig("Student-Performance-Analysis/images/gender-math-score.png")

plt.show()