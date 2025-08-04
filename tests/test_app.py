def test_addition():
    assert 1 + 1 == 2

def test_subtraction():
    assert 5 - 3 == 2

def test_multiply():
    assert 3 * 2 == 6

def test_divide():
    assert 4 / 2 == 2

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        _ = 3 / 0
