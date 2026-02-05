import pytest

def test_case01():
    with pytest.raises(ZeroDivisionError):
        assert (1/0)

def test_case02():
    with pytest.raises(Exception) as excinfo:
        assert (1,2,3) == (1,2,4)
    print(str(excinfo))

def func1():
    raise ValueError("Value is mismatching func1 error")

def test_case03():
    with pytest.raises(Exception) as excpinfo:
        func1()
    print(str(excpinfo))
    assert (str(excpinfo.value)) == "Value is mismatching func2 error"