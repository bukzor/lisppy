from lisppy.lists import S, NIL


def test_list():
    assert [1, 2, 3] == list(S(1, S(2, S(3, NIL))))
