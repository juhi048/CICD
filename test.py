import pytest 
from addition import add
from subtract import sub

def test_add():
    assert add(2,3) == 5

def test_sub():
    assert sub(9,3) == 6

def test_add():
    assert add(1,2) == 3