from utils import arrs


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]


def test_get_new():
     assert arrs.get([1, 2, 3, 5, 8], -2) == None
     assert arrs.get([1, 2, 3, 5, 8], 4) == 8


def test_slice_new():
    assert arrs.my_slice([1, 2, 3, 4]) == [1,2,3,4]
    assert arrs.my_slice([1, 2, 3, 4], 1, 890) == [2,3,4]
    assert arrs.my_slice([1, 2, 3, 4], -1234, 890) == [1, 2, 3, 4]
    assert arrs.my_slice([1, 2, 3, 4], 0, 0) == []
    assert arrs.my_slice([1, 2, 3, 4], -1, 0) == []
    assert arrs.my_slice([], -1, 0) == []

