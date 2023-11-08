import sys
from plates import is_valid

def test_plates1():
    try:
        assert is_valid("ECTO88") == True
    except AssertionError:
        sys.exit(1)

def test_plates2():
    try:
        assert is_valid("CS50P2") == False
    except AssertionError:
        sys.exit(1)

def test_plates3():
    try:
        assert is_valid("NRVOUS") == True
    except AssertionError:
        sys.exit(1)

def test_plates4():
    try:
        assert is_valid("CS50") == True
    except AssertionError:
        sys.exit(1)

def test_plates5():
    try:
        assert is_valid("CS05") == False
    except AssertionError:
        sys.exit(1)

def test_plates6():
    try:
        assert is_valid("ABCDEFGH") == False
    except AssertionError:
        sys.exit(1)

def test_plates7():
    try:
        assert is_valid("1234AB") == False
    except AssertionError:
        sys.exit(1)

def test_plates8():
    try:
        assert is_valid("PI3.14") == False
    except AssertionError:
        sys.exit(1)


def test_plates9():
    try:
        assert is_valid("50") == False
    except AssertionError:
        sys.exit(1)

def test_plates10():
    try:
        assert is_valid(", .H") == False
    except AssertionError:
        sys.exit(1)

def test_plates11():
    try:
        assert is_valid("&%&^") == False
    except AssertionError:
        sys.exit(1)

def test_plates12():
    try:
        assert is_valid("H") == False
    except AssertionError:
        sys.exit(1)

def test_plates13():
    try:
        assert is_valid("OUTATIME") == False
    except AssertionError:
        sys.exit(1)