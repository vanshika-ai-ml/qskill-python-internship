# Matrix Operations Tool

A Python-based interactive command-line application that performs various matrix operations using the NumPy library.

## Features

- Addition of two matrices
- Subtraction of two matrices
- Matrix multiplication
- Transpose of matrices
- Determinant calculation
- Inverse calculation
- Trace calculation
- Scalar multiplication
- Display current matrices
- Enter new matrices without restarting the program
- Supports matrices of different dimensions
- Supports integer and decimal matrix elements
- Input validation for invalid values
- Error handling for incompatible matrix operations
- Interactive menu-driven interface

## Technologies Used

- Python
- NumPy

## How It Works

1. The user enters the number of rows and columns for two matrices.
2. The user enters the elements of both matrices.
3. An interactive menu displays the available matrix operations.
4. The user selects an operation.
5. The program checks whether the selected operation is possible.
6. The result is displayed.
7. The menu continues to run until the user selects Exit.

## Matrix Operations Available

1. Addition
2. Subtraction
3. Multiplication
4. Transpose
5. Determinant
6. Inverse
7. Trace
8. Scalar Multiplication
9. Display Matrices
10. Enter New Matrices
11. Exit

## Requirements

- Python 3.x
- NumPy

Install NumPy using:

pip install numpy

## How to Run

Open the project folder and run:

python main.py

## Input Validation

- Matrix dimensions must be positive natural numbers.
- Matrix elements must be numeric values.
- Menu choices must be numeric.
- Scalar values must be numeric.
- Addition and subtraction require matrices of the same dimensions.
- Matrix multiplication requires the number of columns of Matrix 1 to be equal to the number of rows of Matrix 2.
- Determinant, inverse, and trace operations are validated according to matrix requirements.

## Project Purpose

This project was developed as part of a Python Development Internship task to demonstrate the practical use of Python, NumPy, functions, loops, conditional statements, exception handling, input validation, and matrix operations.

## Author

Vanshika