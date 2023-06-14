def main(str):
    result = convert(str)
    if  7 <= result <= 8:
        print("breakfast time ") 
    elif 12 <= result <= 13:
        print("lunch time")
    elif 18 <= result <= 19:
        print("dinner time")

def convert(time):
    time, mode = time.split(" ")
    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = int(minutes)
    if mode.startswith("p"):
        hours = hours + 12
    decimal_time = hours + minutes / 60
    return decimal_time

user_input = input("What time is it? ")
main(user_input)