def add_numbers(num1, num2):
    result = num1 + num2
    return result

def main():
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))
    sum_result = add_numbers(number1, number2)
    print(f"The sum is {sum_result}")

def test_add_numbers():
    assert add_numbers(2,3) == 5
    assert add_numbers(-9,10) == 1
    assert add_numbers(5,50) == 55
    print("All test cases have passed.")

# Call functions only if script is run as a stand-alone application.
if __name__ == "__main__":
    test_add_numbers()
    main()
    
