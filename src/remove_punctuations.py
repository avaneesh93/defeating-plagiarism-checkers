PUNCTUATIONS = ['.', ',', '\'', '"', '?', '!']


def remove_surrounding_punctuations(word):
    if word is None:
        return word

    word = word.strip()

    if not word:
        return word

    while word[0] in PUNCTUATIONS:
        word = word[1:]

    while word[-1] in PUNCTUATIONS:
        word = word[:-1]

    return word


if __name__ == '__main__':
    word = ".test,"
    print(remove_surrounding_punctuations(word))
