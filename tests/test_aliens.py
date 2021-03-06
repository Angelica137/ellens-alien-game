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
    Alien.total_aliens_created == 0
    a_1 = Alien(5, 1)
    assert a_1.total_aliens_created() == 8
    a_2 = Alien(3, 0)
    assert a_2.total_aliens_created() == 9
    a_3 = [Alien(-2, 6)]
    assert a_3[0].total_aliens_created() == 10


def test_new_aliens_collection():
    locations = [(0, 0), (1, 2)]
    assert (new_aliens_collection(locations)[0].x_coordinate) == 0
    assert (new_aliens_collection(locations)[1].y_coordinate) == 2
