import numpy as np
def input_matrix(name):
    # Get matrix dimensions safely
    while True:
        try:
            rows = int(input(f"Enter rows of {name}: "))
            cols = int(input(f"Enter columns of {name}: "))
            if rows <= 0 or cols <= 0:
                print("Rows and columns must be greater than 0.\n")
                continue
            break
        except ValueError:
            print("Please enter valid integer values.\n")
    matrix = []
    print(f"\nEnter values for {name}")
    print(f"Each row must contain exactly {cols} numbers separated by spaces.")
    print("Example:", " ".join(["1"] * cols))
    print()
    for i in range(rows):
        while True:
            try:
                row = list(map(float, input(f"Row {i+1}: ").split()))
                if len(row) != cols:
                    print(f"\nYou entered {len(row)} value(s).")
                    print(f"Please enter exactly {cols} values separated by spaces.")
                    print("Example:", " ".join(["1"] * cols))
                    continue
                matrix.append(row)
                break
            except ValueError:
                print("Only numeric values are allowed.")
    return np.array(matrix)
# Input matrices
print("\n===== MATRIX INPUT =====\n")
A = input_matrix("Matrix A")
print()
B = input_matrix("Matrix B")
# Menu Loop
while True:
    print("\n==============================")
    print("      MATRIX OPERATIONS")
    print("==============================")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Transpose Matrix A")
    print("5. Determinant of Matrix A")
    print("6. Display Matrices")
    print("7. Exit")
    try:
        choice = int(input("\nEnter choice: "))
    except ValueError:
        print("Please enter a number between 1 and 7.")
        continue
    # Addition
    if choice == 1:

        if A.shape == B.shape:
            print("\nAddition Result:")
            print(A + B)
        else:
            print("\nAddition requires both matrices to have the same dimensions.")
    # Subtraction
    elif choice == 2:
        if A.shape == B.shape:
            print("\nSubtraction Result:")
            print(A - B)
        else:
            print("\nSubtraction requires both matrices to have the same dimensions.")
    # Multiplication
    elif choice == 3:
        if A.shape[1] == B.shape[0]:
            print("\nMultiplication Result:")
            print(np.matmul(A, B))
        else:
            print("\nMultiplication requires:")
            print("Columns of Matrix A = Rows of Matrix B")
    # Transpose
    elif choice == 4:
        print("\nTranspose of Matrix A:")
        print(A.T)
    # Determinant
    elif choice == 5:
        if A.shape[0] == A.shape[1]:
            print("\nDeterminant of Matrix A:")
            print(np.linalg.det(A))
        else:
            print("\nDeterminant can only be calculated for a square matrix.")
    # Display matrices
    elif choice == 6:
        print("\nMatrix A:")
        print(A)
        print("\nMatrix B:")
        print(B)
    # Exit
    elif choice == 7:
        print("\nProgram Ended Successfully.")
        break
    else:
        print("Invalid choice. Please select between 1 and 7.")