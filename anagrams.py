helicopter = "helicopter"
anagram = "tercoplihe"
notanagram = "helicupter"

ANAGRAM = "anagram"
NOT_ANAGRAM = "not anagram"


def check_anagram(word, test):
    if len(word) != len(test):
        return NOT_ANAGRAM

    word_dict = {}
    for ch in word:
        if ch in word_dict:
            word_dict[ch] += 1
        else:
            word_dict[ch] = 1

    test_dict = {}
    for ch in test:
        if ch in word_dict:
            if ch in test_dict:
                test_dict[ch] += 1
            else:
                test_dict[ch] = 1
        else:
            return NOT_ANAGRAM

    for ch, freq in test_dict.items():
        if freq != word_dict.get(ch, 0):
            return NOT_ANAGRAM

    return ANAGRAM


print check_anagram(helicopter, notanagram)
