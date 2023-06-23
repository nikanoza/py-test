def main():
    str = input("Input: ")
    print(f"Output: {shorten(str)}")

def shorten(str):
    result = ""
    vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
    for c in str:
        if c not in vowels:
            result += c
    return result

if __name__ == "__main__":
    main()