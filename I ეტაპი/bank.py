def main():
    user_input = input("Greeting: ")
    print(bank(user_input))
    
def bank(string):
    result = string.lstrip().lower()
    if result.startswith("hello"):
        return("$0")
    elif result.startswith("h") and not result.startswith("hello"):
        return("$20")
    else:
        return("$100")

if __name__ == "__main__":
    main()