def vowel_count(input_str):
    num_vowels = 0
    for letter in input_str:
        if letter in "aeiou":
            num_vowels += 1
    return num_vowels