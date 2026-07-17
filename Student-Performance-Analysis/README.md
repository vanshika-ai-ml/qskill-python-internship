# Student Performance Analysis

## Overview

This project analyzes student performance using **Python, Pandas, NumPy, and Matplotlib**. It loads a CSV dataset, performs basic data analysis, and generates multiple visualizations to better understand students' academic performance.

## Features

- Load and read CSV dataset
- Display first 5 records
- Check dataset shape
- Identify missing values
- Display dataset information
- Calculate average scores
- Find highest and lowest math scores
- Generate histogram of math scores
- Generate bar chart of average subject scores
- Generate scatter plot of reading vs writing scores
- Generate gender-wise average math score chart
- Automatically save all generated graphs

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib

## Dataset

- StudentsPerformance.csv

## Project Structure

```
Student-Performance-Analysis/
│── images/
│   ├── average-scores.png
│   ├── gender-math-score.png
│   ├── math-score-distribution.png
│   └── reading-vs-writing.png
│── main.py
│── StudentsPerformance.csv
│── README.md
```

## How to Run

1. Install the required libraries:

```bash
pip install pandas numpy matplotlib
```

2. Run the project:

```bash
python main.py
```

## Output

The program displays:

- Dataset preview
- Dataset shape
- Missing values
- Dataset information
- Average scores
- Highest and lowest math scores

It also generates and saves the following visualizations:

- Math Score Distribution
- Average Scores Comparison
- Reading vs Writing Scatter Plot
- Gender-wise Average Math Score

## Future Improvements

- Add more visualizations
- Perform correlation analysis
- Build machine learning models for score prediction
- Create an interactive dashboard

## Author

**Vanshika**