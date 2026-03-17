
#matrix calculation

def printmatx(matrix, label="Matrix"):
    print(f"\n  {label}:")
    col_widths = []
    for j in range(len(matrix[0])):
        w = max(len(str(matrix[i][j])) for i in range(len(matrix)))
        col_widths.append(w)
    for row in matrix:
        print("  | " + "  ".join(str(row[j]).rjust(col_widths[j]) for j in range(len(row))) + " |")


def input_matrix(name=""):
    label = f" for {name}" if name else ""
    rows = int(input(f"  Enter number of rows{label}: "))
    cols = int(input(f"  Enter number of columns{label}: "))
    matrix = []
    print(f"  Enter values row by row (space-separated, {cols} values each):")
    for i in range(rows):
        while True:
            try:
                row = list(map(float, input(f"    Row {i+1}: ").split()))
                if len(row) != cols:
                    print(f"please enter exactly {cols} values.")
                    continue
                matrix.append(row)
                break
            except ValueError:
                print("invalid input. Please enter numbers only.")
    return matrix


#Addition & Subtraction

def addition(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        raise ValueError("matrices must have the same dimensions for addition.")
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def subtraction(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        raise ValueError("Matrices must have the same dimensions for subtraction.")
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


#  (b) Matrix Multiplication

def multiplication(A, B):
    if len(A[0]) != len(B):
        raise ValueError("Columns of A must equal rows of B for multiplication.")
    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(B[0])):
            s = 0
            for k in range(len(B)):
                s += A[i][k] * B[k][j]
            row.append(s)
        result.append(row)
    return result


# c) Transpose

def transpose(A):
    return [[A[i][j] for i in range(len(A))] for j in range(len(A[0]))]


#  (d) Determinant (2×2 and 3×3)

def determinant(A):
    rows, cols = len(A), len(A[0])
    if rows != cols:
        raise ValueError("Determinant is only defined for square matrices.")
    if rows == 2:
        return A[0][0] * A[1][1] - A[0][1] * A[1][0]
    if rows == 3:
        return (
            A[0][0] * (A[1][1] * A[2][2] - A[1][2] * A[2][1])
          - A[0][1] * (A[1][0] * A[2][2] - A[1][2] * A[2][0])
          + A[0][2] * (A[1][0] * A[2][1] - A[1][1] * A[2][0])
        )
    raise ValueError("determinant only supported for 2x2 and 3x3 matrices.")


# (e) Scalar Multiplication 

def scalar_multiplication(A, scalar):
    return [[A[i][j] * scalar for j in range(len(A[0]))] for i in range(len(A))]




#menu

def print_menu():
    print("\n" + "=" * 50)
    print("     MATRIX CALCULATOR")
    print("=" * 50)
    print("  1. Addition")
    print("  2. Subtraction")
    print("  3. Multiplication")
    print("  4. Transpose")
    print("  5. Determinant (2x2 / 3x3)")
    print("  6. Scalar Multiplication")
    print("  0. Exit")
    print("=" * 50)


def main():
    while True:
        print_menu()
        choice = input("  Enter your choice: ").strip()

        try:
            if choice == "1":
                print("\n  -- Matrix Addition --")
                A = input_matrix("Matrix A")
                B = input_matrix("Matrix B")
                printmatx(addition(A, B), "A + B")

            elif choice == "2":
                print("\n  -- Matrix Subtraction --")
                A = input_matrix("Matrix A")
                B = input_matrix("Matrix B")
                printmatx(subtraction(A, B), "A - B")

            elif choice == "3":
                print("\n  -- Matrix Multiplication --")
                A = input_matrix("Matrix A")
                B = input_matrix("Matrix B")
                printmatx(multiplication(A, B), "A × B")

            elif choice == "4":
                print("\n  -- Matrix Transpose --")
                A = input_matrix("Matrix A")
                printmatx(transpose(A), "Transpose(A)")

            elif choice == "5":
                print("\n  -- Matrix Determinant --")
                A = input_matrix("Matrix A")
                det = determinant(A)
                printmatx(A, "A")
                print(f"\n  det(A) = {det}")

            elif choice == "6":
                print("\n  -- Scalar Multiplication --")
                A = input_matrix("Matrix A")
                s = float(input("  Enter scalar value: "))
                printmatx(scalar_multiplication(A, s), f"{s} × A")  
            elif choice == "0":
                print("  Goodbye!")
                break

            else:
                print("  Invalid choice. Try again.")

        except ValueError as e:
            print(f"  Error: {e}")
        except Exception as e:
            print(f"  Error: {e}")


if __name__ == "__main__":
    main()

