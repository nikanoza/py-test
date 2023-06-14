def calculate(str):
    result = eval(str)
    print(f"{result:.1f}")

user_input = input("Expression: ")
calculate(user_input)