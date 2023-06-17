products = {
    "baja taco": 4.00,
    "burrito": 7.50,
    "bowl": 8.50,
    "nachos": 11.00,
    "quesadilla": 8.50,
    "super burrito": 8.50,
    "super quesadilla": 9.50,
    "taco": 3.00,
    "tortilla salad": 8.00
}

def main():
    try:
        sum = 0
        while True:
            user_input = input("item: ")
            if user_input.lower() in products:
                sum += products[user_input]
                print(f"Total: ${sum:.2f}")
    except KeyboardInterrupt:
        pass
main()
