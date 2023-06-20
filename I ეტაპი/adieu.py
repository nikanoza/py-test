def main():
    names = [];
    try:
        while True:
            user_input = input("item: ")
            if user_input.lower() in products:
                sum += products[user_input]
                print(f"Total: ${sum:.2f}")
    except KeyboardInterrupt:
        pass
main()