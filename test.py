import ordered


@ordered.ordered()
class A(object):
    x = 1
    y = 2
    z = 3


def test_ordered():
    assert A.x == 1
    assert A.y == 2
    assert A.z == 3
    assert A._order == ['x', 'y', 'z']
