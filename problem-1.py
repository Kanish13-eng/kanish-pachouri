class Calculator:

    def calculate(self, a, b, operation):
        operation = operation.lower()

        if operation == "add" or operation == "+":
            return a + b

        elif operation == "subtract" or operation == "-":
            return a - b

        elif operation == "multiply" or operation == "*":
            return a * b

        elif operation == "divide" or operation == "/":
            if b == 0:
                print("Error: Division by zero is not allowed.")
                return None
            return a / b

        else:
            print("Invalid operation type.")
            return None


calc = Calculator()

a = 10.5
b = 2.5
operation = "multiply"

result = calc.calculate(a, b, operation)

print("Result:", result)
