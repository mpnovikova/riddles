import copy


def permutations(word):
    if len(word) == 1:
        return word

    if len(word) == 2:
        return [word, word[::-1]]

    result = []
    for ch in word:
        word_copy = copy.copy(word)
        word_copy.remove(ch)
        perms = permutations(word_copy)
        for p in perms:
            result.append(ch + ''.join(p))

    return result


res = permutations(list("abc"))
print res
print len(res)
