user_input = input("Tell me something: ")

transform_input = user_input.replace(":)", "\U0001F600").replace(":(", "\U0001F61E")
print(transform_input)