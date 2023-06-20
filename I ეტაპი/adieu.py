def main():
    names = []
    try:
        while True:
            user_input = input("name: ")
            names.append(user_input)
    except EOFError:
        result = "Adieu, adieu, to"
        for index, name in enumerate(names):
            if index + 1 < len(names):
                result += f" {name},"
            else:
                result += f" and {name}"
        print(result)

main()