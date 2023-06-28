from project import game
from project import check
from project import random_cards
from project import user_choice
from project import combination

def main():
    test_check()
    test_random_cards()

def test_check():
    assert check(3, 5, True) == True
    assert check(3, 5, False) == False
    assert check(5, 3, False) == True
    assert check(5, 3, True) == False
    assert check(3, 3, False) == False
    assert check(3, 3, True) == False

def test_random_cards():
    assert 0 <= random_cards() <= len(combination)

def test_user_choice():
    result = user_choice()
    assert result == True or result == False

if __name__ == "__main__":
    main()