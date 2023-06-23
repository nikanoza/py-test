from bank import bank

def test_zero():
    assert bank("hello") == "$0"
    assert bank("Hello, my dear") == "$0"

def test_twenty():
    assert bank("hi nika") == "$20"
    assert bank("Hi nika") == "$20"
    assert bank("Hell yes") == "$20"

def test_more():
    assert bank("my name is") == "$100"
    assert bank("test is test") == "$100"
    assert bank("every dumb") == "$100"

def main():
    test_more()
    test_twenty()
    test_more()

if __name__ == "__main__":
    main()    