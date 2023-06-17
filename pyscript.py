# Function that accepts two numbers, adds them and returns the result.
def addTwoNum(num1, num2):
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        raise ValueError("Both inputs must be numbers.")
    result = num1 + num2
    return result

# Prompts user for input and validates it.
def main():
    print("Two numbers will be added.")
    # Loop until valid numbers are given
    while True:
        number1 = input("The first number? ")
        number2 = input("The second number? ")
    # Make sure numbers are entered.
        try:
            number1 = float(number1)
            number2 = float(number2)
            break # Exit loop
    # Show error if numbers were not given.
        except ValueError: # Numbers were not given
            print("Invalid input. Enter numbers only.")
    sum_result = addTwoNum(number1, number2)
    print(f"The sum is {sum_result}")

# Tests addTwoNum() for expected functionality. An AssertionError will be raised if addTwoNum produced an unexpected result.
def test_addTwoNum():
    assert addTwoNum(2,3) == 5
    assert addTwoNum(-9,10) == 1
    # addTwoNum() Should not accept text input.
    try:
            addTwoNum("Four","Five")
    except ValueError:
            pass
    else:
        raise AssertionError("Expected a ValueError.")
    print("All test cases have passed.")

# Functions will not be called if this script is imported.
if __name__ == "__main__":
    test_addTwoNum()
    main()   
