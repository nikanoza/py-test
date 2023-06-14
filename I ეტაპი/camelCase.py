def main(str):
    result = ""
    for char in str:
        if char.isupper():
            result += "_" + char.lower()
        else:
            result += char
    print("snake_case:", result)

user_input = input("camelCase: ")
main(user_input)