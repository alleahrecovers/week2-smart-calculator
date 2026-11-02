def basic_calculate():
    # Ask the user for two numbers and a math operation.
    # Support addition, subtraction, multiplication, and division.
    # Display the answer and handle invalid input and division by zero.

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Enter the operation (+, -, *, /): ")

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
                return
            result = num1 / num2
        else:
            print("Error: Invalid operation. Please use +, -, *, or /.")
            return

        print(f"The result of {num1} {operation} {num2} is: {result}") 
    except ValueError:
        print("Error: Please enter valid numbers.") 


 # Create a function called solve_for_x(a, b).
# Use brute-force search to find an approximate solution to ax + b = 0.
# Try every x value from -100 to 100 in steps of 0.1.
# Keep track of the x value that makes the equation closest to zero.
# Return the best x value and its error.


def solve_for_x(a, b):
    best_x = 0
    min_error = float('inf')

    for x in [i * 0.1 for i in range(-1000, 1001)]:
        error = abs(a * x + b)
        if error < min_error:
            min_error = error
            best_x = x

    return best_x, min_error    


# Create a function called equation_solver_menu().
# Ask the user to enter the coefficients a and b for an equation ax + b = 0.
# Call solve_for_x(a, b) to find the approximate solution.
# Display the closest x value and its error.
# Handle invalid numeric input.


def equation_solver_menu():
    try:
        a = float(input("Enter the coefficient a for the equation ax + b = 0: "))
        b = float(input("Enter the coefficient b for the equation ax + b = 0: "))
        x, error = solve_for_x(a, b)
        print(f"The closest x value is: {x}")
        print(f"The error is: {error}")
    except ValueError:
        print("Error: Please enter valid numbers.") 


# Create a function called visualize_search(a, b).
# Search for x values from -100 to 100 in steps of 0.1.
# Calculate the error using abs(a * x + b).
# Print each x value tested and its error.
# Keep track of the x value with the smallest error.
# Display the best x value and its error at the end.


def visualize_search(a, b):
    best_x = 0
    min_error = float('inf')

    for x in [i * 0.1 for i in range(-1000, 1001)]:
        error = abs(a * x + b)
        print(f"x = {x}, error = {error}")
        if error < min_error:
            min_error = error
            best_x = x

    print(f"The best x value is: {best_x}")
    print(f"The error is: {min_error}") 


# Create the main program with an interactive menu.
# Display five options: basic calculation, equation solver,
# search visualization, explanation of search algorithms, and exit.
# Use a while loop so the menu keeps appearing until the user exits.
# Call the correct function based on the user's selection.
# Ask for equation coefficients when using search visualization.
# Handle invalid menu selections.

def main():
    while True:
        print("\nSmart Calculator Menu")
        print("1. Basic Calculation")
        print("2. Equation Solver")
        print("3. Search Visualization")
        print("4. Explanation of Search Algorithms")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            basic_calculate()

        elif choice == "2":
            equation_solver_menu()

        elif choice == "3":
            try:
                a = float(input("Enter coefficient a: "))
                b = float(input("Enter coefficient b: "))
                visualize_search(a, b)

            except ValueError:
                print("Error: Please enter valid numbers.")

        elif choice == "4":
            print("\nExplanation of Search Algorithms:")
            print("A brute-force search tests many possible values")
            print("until it finds the closest answer.")
            print("In this calculator, we test values from -100 to 100")
            print("in steps of 0.1.")
            print("This method is simple but can take many attempts.")

        elif choice == "5":
            print("Thank you for using the Smart Calculator!")
            break

        else:
            print("Invalid choice. Please select a number from 1 to 5.")



main()