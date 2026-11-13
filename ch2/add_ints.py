"""Add two integers"""

def main() -> None:
    """Reads two ints from the user, adds them and prints the result"""

    # Data input
    num1 = int(input("Enter first integer: "))
    num2 = int(input("Enter second integer: "))

    # Add the two ints
    result = num1 + num2

    # Print the result
    print(f"Result is {result}")