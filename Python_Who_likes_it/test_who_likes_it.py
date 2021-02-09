from who_likes_it import likes

def test_one_person():
    answer = likes(["Peter"])
    assert answer == "Peter likes this"

def test_two_people():
    answer = likes(["Jacob", "Alex"])
    assert answer == "Jacob and Alex like this"

def test_three_people():
    answer = likes(["Max", "John", "Mark"])
    assert answer == "Max, John and Mark like this"

def test_more_than_three_people():
    answer = likes(["Alex", "Jacob", "Mark", "Max"])
    assert answer == "Alex, Jacob and 2 others like this"

def test_no_one():
    answer = likes([])
    assert answer == "no one likes this"