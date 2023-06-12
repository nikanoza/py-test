# I დავალება

name = input("What is your name?")
print("Hello,", name ,", nice to meet you!")

print("Hello,", input("What is your name?") ,", nice to meet you!")

nameInput = input("What is your name?")
length = len(nameInput)

match length:
    case 3:
        print("hello", nameInput, "nice to meet you")
    case 4:
        print("Hello my friend", nameInput, "how are you?")
    case 5:
        print("Hello", nameInput, "can you be my friend?")
    case _:
        print(nameInput, "you are so ugly")