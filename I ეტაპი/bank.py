def main(string):
    result = string.lstrip().lower()
    if result.startswith("hello"):
        print("$0")
    elif result.startswith("h") and not result.startswith("hello"):
        print("$20")
    else:
        print("$100")

user_input = input("Greeting: ")
main(user_input)