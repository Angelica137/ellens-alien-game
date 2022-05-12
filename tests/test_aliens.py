from scripts.aliens import *


def test_alien_has_x_y_coordinates():
    a = Alien(2, 0)
    assert a.x_coordinate == 2
    assert a.y_coordinate == 0


def test_alien_health_is_3():
    a = Alien(2, 0)
    assert a.health == 3


def test_alien_hit_reduces_health_by_1():
    a = Alien(2, 0)
    a.hit()
    assert a.health == 2


def test_alien_hit_health_is_0():
    a = Alien(2, 0)
    a.health = 0
    a.hit()
    assert a.health == 0


def test_is_alive_True():
    a = Alien(1, 0)
    assert a.is_alive() == True


def test_is_alive_False():
    a = Alien(0, 0)
    a.health = -1
    assert a.is_alive() == False


def test_teleport():
    a = Alien(0, 0)
    a.teleport(5, -4)
    assert a.x_coordinate == 5
    assert a.y_coordinate == -4


def test_total_aliens_created():
    a_1 = Alien(5, 1)
    a_1.total_aliens_created() == 1
