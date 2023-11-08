import sys
from bank import value

def test_value():
    # try:
    assert value("Newman I'm your husband") == 100
    # except AssertionError:
        # sys.exit()

# def test_value20():
    # try:
    assert value("Hi") == 20
    # except AssertionError:
        # sys.exit()

# def test_value0():
    # try:
    assert value("Hello") == 0
    # except AssertionError:
        # sys.exit()



if __name__ == "__main__":
    try:
        # test_value100()
        # test_value20()
        test_value()
        sys.exit(0)
        # break

    except AssertionError:
        # If all tests pass, exit with status code 0
        sys.exit(1)