from middle import get_middle

def test_returns_a_single_character():
    answer = get_middle("A")
    assert answer == "A"

def test_returns_middle_character_if_odd():
    answer = get_middle("tests")
    assert answer == "s"

def test_returns_two_middle_characters_if_even():
    answer = get_middle("test")
    assert answer == "es"