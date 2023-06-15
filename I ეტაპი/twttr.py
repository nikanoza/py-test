def main(str):
    result = ""
    vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
    for c in str:
        if c not in vowels:
            result += c
    print(f"Output: {result}")

user_input = input("Input: ")
main(user_input)