def vowel_count(input_str):
    num_vowels = 0
    for vowel in input_str:
        if vowel in "aeiou":
            num_vowels += 1
    return num_vowels