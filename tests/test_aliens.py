from scripts.aliens import *


def test_instantiate_alien_object():
    a = Alien()
    assert type(a) == Alien


def test_alien_has_x_y_coordinates():
    a = Alien(2, 0)
    assert a.x_coordinate == 2
