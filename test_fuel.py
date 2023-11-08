import sys
import pytest
from fuel import convert, gauge



def test_fuel3():
    try:
        assert convert('1/4') == 25
        assert gauge(25) == "25%"
    except AssertionError:
        sys.exit(1)


def test_fuel4():
    try:
        assert convert('1/2') == 50
        assert gauge(50) == "50%"
    except AssertionError:
        sys.exit(1)

def test_fuel5():
    try:
        assert convert('99/100') == 99
        assert gauge(99) == "F"
    except AssertionError:
        sys.exit(1)

def test_fuel6():
    try:
        assert convert('1/100') == 1
        assert gauge(1) == "E"
    except AssertionError:
        sys.exit(1)




def test_convert():
    with pytest.raises(ZeroDivisionError):
        convert('100/0')

def test_valid_type():
    with pytest.raises(ValueError):
        convert('three/four')