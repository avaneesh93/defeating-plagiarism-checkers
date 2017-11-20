import re

import wikipedia as w
from nltk import sent_tokenize
from wikipedia.exceptions import DisambiguationError


def get_sentences_from_wiki(wiki_pages=1, print_sentence=False):
    titles = w.random(wiki_pages)

    result = []

    for title in titles:
        try:
            page = w.page(title=title)

            for sentence in sent_tokenize(page.content):
                if skip_sentence(sentence):
                    continue

                result.append(sentence)
                if print_sentence:
                    print(sentence)

        except DisambiguationError:
            pass

    return result


def skip_sentence(sentence, min_words=10):
    # Skip sentences with less than the specified amount of words
    if len(sentence.split()) < min_words:
        return True

    # Skip sentences that DON'T start with a capital letter and DON'T end with a period
    if not re.search(r'(?<=^[A-Z]).+(?=\.$)', sentence):
        return True

    # Skip sentences with numbers in them
    if re.search(r'\d', sentence):
        return True

    # Skip sentences with capital letters in them (probably proper nouns),
    #  except the first letter.
    if re.search(r'[A-Z]', sentence[1:]):
        return True


if __name__ == '__main__':
    get_sentences_from_wiki(wiki_pages=100, print_sentence=True)
