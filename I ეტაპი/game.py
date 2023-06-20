import random

def main():
    level = 0
    while True:
        user_input = input("Level: ")
        if int(user_input) >= 1:
            level = int(user_input)
            break
    random_number = random.randint(1, level)
    guess = 0
    while random_number != guess:
        user_guess = input("Guess: ")
        if int(user_guess) > random_number:
            print("Too large!")
        elif int(user_guess) < random_number:
            print("Too small!")
        elif int(user_guess) == random_number:
            print("Just right!")
            break

main()