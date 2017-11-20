import re

import wikipedia as w
from nltk import sent_tokenize
from wikipedia.exceptions import DisambiguationError


def get_sentences_from_wiki(wiki_pages=1):
    titles = w.random(wiki_pages)

    result = []

    for title in titles:
        try:
            page = w.page(title=title)

            for sentence in sent_tokenize(page.summary):
                # Skip sentences with numbers in them
                if re.search(r'\d', sentence):
                    continue

                result.append(sentence)

        except DisambiguationError:
            pass

    return result


if __name__ == '__main__':
    for s in get_sentences_from_wiki(wiki_pages=10):
        print(s)
