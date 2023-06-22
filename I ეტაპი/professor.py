import random

def main():
    level = 0
    score = 0
    while True:
        user_input = int(input("level: "))
        if 1 <= user_input <= 3:
            level = user_input
            break
    for i in range(10):
        first = random.randint(1, 20)
        second = random.randint(1, 20)
        result = first + second
        tryAmount = 0
        while True:
            if tryAmount == 3:
                print(f"{first} + {second} = {result}")
                break
            answer = int(input(f"{first} + {second} = "))
            if answer == result:
                score += 1
                break
            else:
                print("EEE")
                tryAmount += 1
    print(f"score: {score}")

main()
            