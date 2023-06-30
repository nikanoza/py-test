import random

combination = ["2","3","4","5","6","7","8","9","10", "J", "Q", "K", "T"]


def game():
    score = 0
    start = random_cards()
    while True:
        print(f"card: {combination[start]}")
        user = user_choice()
        random_element_index = random_cards()
        result = check(start, random_element_index, user)
        if(result):
            score += 1
            start = random_element_index
        else:
            break
    print(f"Your score is: {score}")

def check(start, next, user):
    return (user and next > start) or (not user and next < start)


def random_cards():
    random_element = random.choice(combination)
    random_index = combination.index(random_element)
    return random_index

def user_choice():
    user_input = False
    while user_input != "high" and user_input != "low":
        user_input = input("high or low ? ").lower()
    return user_input == "high"

if __name__ == "__main__":
    game()
