from scripts.aliens import *


def test_alien_has_x_y_coordinates():
    a = Alien(2, 0)
    assert a.x_coordinate == 2
    assert a.y_coordinate == 0


def test_alien_hhealth_is_3():
    a = Alien(2, 0)
    assert a.health == 3
