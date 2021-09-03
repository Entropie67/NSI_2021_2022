import pytest
from fonctions import factorielle


def test_0():
    assert factorielle(5) == 120

def test_1():
    assert factorielle(0) == 1

def test_2():
    assert factorielle(3) == 6