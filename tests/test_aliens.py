from scripts.aliens import *


def test_instantiate_alien_object():
    a = Alien()
    assert type(a) == Alien
