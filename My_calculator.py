print("Calculator.")
print("""In our calculator, you can perform the following operations: 
      addition ('+'),\n substraction ('-'),\n multiplication ('*')\n and division('/').""")

permitted_operations = ["+", "-", "*", "/"]


def choose_operation():
    while True:
        operation = input(f"Type the operation you want to perform: {permitted_operations}")
        if operation not in permitted_operations:
            print("This operation is not permitted.")
            continue
    return operation


def get_number(question):
    while True:
        try:
            number = float(input(question))
            return number
        except ValueError:
            print("You must enter a valid number.")

def addition(n1, n2):
    return n1 + n2

def substraction(n1, n2):
    return n1 - n2

def multiplication(n1, n2):
    return n1 * n2

def division(n1, n2):
    try:
        return n1 / n2
    except ZeroDivisionError:
        print("You cannot divide by zero.")


def calculator():
    first_num = get_number("Type the first number: ")

    while True:
        operation = choose_operation()
        second_num = get_number("Type the second number: ")
        if operation == "+":
            result = addition(first_num, second_num)
        elif operation == "-":
            result = substraction(first_num, second_num)
        elif operation == "*":
            result = multiplication(first_num, second_num)
        elif operation == "/":
            result = division(first_num, second_num)
            if result is None:
                continue

        print(f"{first_num} {operation} {second_num} = {result}")
        return result


def decision_to_continue():
        result = calculator()
        while True:
            decision = input(f"Type 'yes' to continue calculating with {result}, type 'no' to start a new calculation: ")
            try:
                if decision == "yes":
                    operation = choose_operation()
                    second_num = get_number("Type another number: ")
                    if operation == "+":
                        result = addition(result, second_num)
                    elif operation == "-":
                        result = substraction(result, second_num)
                    elif operation == "*":
                        result = multiplication(result, second_num)
                    elif operation == "/":
                        temp_result = division(result, second_num)
                        if temp_result is None:
                            continue

                elif decision == "no":
                    print("\n" * 30)   # sprawdzić dlaczego nie wykonuje się
                    main()
            except Exception:
                print("Incorrect command.")
                continue
        return result

def main():
    while True:
        try:
            if input("Press Enter to continue, or type 'exit' to quit: ").lower() == "exit":
                print("Goodbye!")
                break
            else:
                decision_to_continue()
        except:
            print("Incorrect command.")
            continue

