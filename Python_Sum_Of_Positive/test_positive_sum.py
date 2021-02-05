from positive_sum import positive_sum


def test_positive_sum_one():
    solution = positive_sum([1,-4,7,12])
    assert solution == 20

def test_positive_sum_two():
    solution2 = positive_sum([1,2,3,4,5])
    assert solution2 == 15

def test_positive_sum_three():
    solution3 = positive_sum([])
    assert solution3 == 0

def test_positive_sum_four():
    solution4 = positive_sum([-1,-2,-3,-4,-5])
    assert solution4 == 0