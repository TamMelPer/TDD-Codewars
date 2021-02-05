from vowel_count import vowel_count

def test_vowel_count_with_all_vowels():
    count = vowel_count("aeiou")
    assert count == 5

def test_vowel_count_with_no_vowels():
    count = vowel_count("")
    assert count == 0

def test_vowel_count_with_mix_of_vowels_and_consonants():
    count = vowel_count("abracadabra")
    assert count == 5

def test_vowel_count_with_only_consonants():
    count = vowel_count("bcdfgh")
    assert count == 0