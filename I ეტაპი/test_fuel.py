from fuel import fuel

def main():
    assert fuel("3/3") == "F"
    assert fuel("5/5") == "F"
    assert fuel("0/3") == "E"
    assert fuel("0/5") == "E"
    assert fuel("3/5") == 60
    assert fuel("3/4") == 75

if __name__ == "__main__":
    main()    