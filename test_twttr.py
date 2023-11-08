import sys
from twttr import shorten

def test_twttr():
    try:
        assert shorten("Uditha") == "dth"
        assert shorten("What's up ma bro?") == "Wht's p m br?" 
        assert shorten("12345") == "12345"
    except:
        sys.exit(1)