import numpy as np


def input_matrix(name):

    while True:
        try:
            rows = int(input(f"\nEnter number of rows for {name}: "))
            cols = int(input(f"Enter number of columns for {name}: "))

            if rows > 0 and cols > 0:
                  break
            else:
                  print("Invalid input! Please enter natural numbers only.")

        except ValueError:
               print("Invalid input! Please enter natural numbers only.")
    

    matrix = []

    print(f"\nEnter elements for {name}")

    for i in range(rows):

        row = []

        for j in range(cols):

            while True:
               try:
                   value = float(input(f"Element [{i+1}][{j+1}]: "))
                   break
               except ValueError:
                   print("Invalid input! Please enter a numeric value only.")

            row.append(value)

        matrix.append(row)

    return np.array(matrix)

print("======================================")
print("      MATRIX OPERATIONS TOOL")
print("======================================")

matrix1 = input_matrix("Matrix 1")
matrix2 = input_matrix("Matrix 2")

while True:

    print("\n======================================")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Transpose")
    print("5. Determinant")
    print("6. Inverse")
    print("7. Trace")
    print("8. Scalar Multiplication")
    print("9. Display Matrices")
    print("10. Enter New Matrices")
    print("11. Exit")
    print("======================================")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("\nInvalid input! Please enter a number between 1 and 11.")
        continue

    # Addition
    if choice == 1:

        if matrix1.shape == matrix2.shape:

            print("\nResult (Addition):")
            print(matrix1 + matrix2)

        else:
            print("\nAddition is not possible. Matrix sizes must be same.")

    # Subtraction
    elif choice == 2:

        if matrix1.shape == matrix2.shape:

            print("\nResult (Subtraction):")
            print(matrix1 - matrix2)

        else:
            print("\nSubtraction is not possible. Matrix sizes must be same.")

    # Multiplication
    elif choice == 3:

        if matrix1.shape[1] == matrix2.shape[0]:

            print("\nResult (Multiplication):")
            print(np.dot(matrix1, matrix2))

        else:
            print("\nMultiplication is not possible.")
            print("Columns of Matrix 1 must be equal to Rows of Matrix 2.")

            # Transpose
    elif choice == 4:

        print("\nTranspose of Matrix 1:")
        print(matrix1.T)

        print("\nTranspose of Matrix 2:")
        print(matrix2.T)

    # Determinant
    elif choice == 5:

        if matrix1.shape[0] == matrix1.shape[1]:
            print("\nDeterminant of Matrix 1:")
            print(np.linalg.det(matrix1))
        else:
            print("\nMatrix 1 is not square. Determinant cannot be calculated.")

        if matrix2.shape[0] == matrix2.shape[1]:
            print("\nDeterminant of Matrix 2:")
            print(np.linalg.det(matrix2))
        else:
            print("\nMatrix 2 is not square. Determinant cannot be calculated.")

    # Inverse
    elif choice == 6:

        if matrix1.shape[0] == matrix1.shape[1] and not np.isclose(np.linalg.det(matrix1),0):         
             print("\nInverse of Matrix 1:")
             print(np.linalg.inv(matrix1))
        else:
            print("\nInverse of Matrix 1 does not exist.")

        if matrix2.shape[0] == matrix2.shape[1] and not np.isclose(np.linalg.det(matrix2),0):
            print("\nInverse of Matrix 2:")
            print(np.linalg.inv(matrix2))
        else:
            print("\nInverse of Matrix 2 does not exist.")

    # Trace
    elif choice == 7:

        if matrix1.shape[0] == matrix1.shape[1]:
            print("\nTrace of Matrix 1:")
            print(np.trace(matrix1))
        else:
            print("\nTrace cannot be calculated for Matrix 1.")

        if matrix2.shape[0] == matrix2.shape[1]:
            print("\nTrace of Matrix 2:")
            print(np.trace(matrix2))
        else:
            print("\nTrace cannot be calculated for Matrix 2.")

            # Scalar Multiplication
    elif choice == 8:

        while True:
            try:
                scalar = float(input("\nEnter scalar value: "))
                break
            except ValueError:
                print("invalid input! Please enter a numeric value only.")
        
        print("\nScalar Multiplication of Matrix 1:")
        print(matrix1 * scalar)

        print("\nScalar Multiplication of Matrix 2:")
        print(matrix2 * scalar)

    # Display Matrices
    elif choice == 9:

        print("\nMatrix 1:")
        print(matrix1)

        print("\nMatrix 2:")
        print(matrix2)

    # Enter New Matrices
    elif choice == 10:

        matrix1 = input_matrix("Matrix 1")
        matrix2 = input_matrix("Matrix 2")

        print("\nMatrices Updated Successfully!")

    # Exit
    elif choice == 11:

        print("\nThank you for using Matrix Operations Tool!")
        break

    # Invalid Choice
    else:

        print("\nInvalid Choice! Please enter a number between 1 and 11.")