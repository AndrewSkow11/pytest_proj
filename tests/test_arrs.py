from utils import arrs
import pytest

@pytest.fixture
def fixture_for_get1():
    return [1, 2, 3]

@pytest.fixture
def fixture_for_get2():
    return [1, 2, 3, 5, 8]

def test_get(fixture_for_get1, fixture_for_get2):
    assert arrs.get(fixture_for_get1, 1, 'test') == 2
    assert arrs.get(fixture_for_get2, -2) == None
    assert arrs.get(fixture_for_get2, 4) == 8
    assert arrs.get([], 0, "test") == "test"

@pytest.fixture
def fixture_for_slice():
    return [1, 2, 3, 4]

def test_slice(fixture_for_slice):
    assert arrs.my_slice(fixture_for_slice, 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice(fixture_for_slice) == [1,2,3,4]
    assert arrs.my_slice(fixture_for_slice, 1, 890) == [2,3,4]
    assert arrs.my_slice(fixture_for_slice, -1234, 890) == [1, 2, 3, 4]
    assert arrs.my_slice(fixture_for_slice, 0, 0) == []
    assert arrs.my_slice(fixture_for_slice, -1, 0) == []
    assert arrs.my_slice([], -1, 0) == []

