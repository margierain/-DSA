# read Pset.md to understand the problem set solved for
def reconstruction_words(_set, _str):
    res = []
    word = ""

    for char in _str:
        word += char
        if word in _set:
            res.append(word)
            word = ""

    if not res: # or if res is zero or empty or False
        return None
    return res

print(reconstruction_words({"quick", "brown", "the", "fox"}, "thequickbrownfox"))
print(reconstruction_words({'bed', 'bath', 'bedbath', 'and', 'beyond'}, "bedbathandbeyond"))
