quotes = {
    "William Shakespeare": "A rose by any other name would smell as sweet.",
    "John Kennedy":"Ask not what your country can do for you; ask what you can do for your country.",
    "Woody Allen":"Eighty percent of success is showing up.",
    "Thomas Edison": "Genius is one percent inspiration and ninety-nine percent perspiration.",
    "Winston Churchill": "If you are going through hell, keep going."
}

def main(str):
    if str in quotes:
        print(f"{str} says, \"{quotes[str]}\"")
    else:
        print("Invalid name entered.")

user_input = input("choose which famous quotes want to show: William Shakespeare, John Kennedy, Woody Allen, Thomas Edison, Winston Churchill : ")

main(user_input)