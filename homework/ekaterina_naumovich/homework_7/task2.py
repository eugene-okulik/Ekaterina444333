words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}

def result():
    for key, value in words.items():
        print(key * value)

result()


words_2 = {'I': 3, 'love': 5, 'Python': 1, '!': 50}
pairs = list(words_2.items())

def result_2():
    i = 0
    while i < len(pairs):
        word, count = pairs[i]
        print(word * count)
        i += 1

result_2()