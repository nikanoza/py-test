def main(string):
    if string == "42" or string == "forty-two" or string == "forty two":
        print("Yes")
    else:
        print("No")
    
user_input = input("What is the Great Question of Life, the Universe and Everything?")
main(user_input)