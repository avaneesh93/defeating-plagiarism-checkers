import re

import wikipedia as w
from nltk import sent_tokenize
from wikipedia.exceptions import DisambiguationError, PageError


def get_sentences_from_wiki(sentences_amount=100, print_sentence=False,
                            save_to_file=False, file_name=None, print_progress=False):
    # Working on the assumption that one page will give at least one sentence averagely
    titles = w.random(sentences_amount)

    result = []

    count = 0

    for title in titles:
        try:
            page = w.page(title=title)

            for sentence in sent_tokenize(page.content):
                if skip_sentence(sentence):
                    continue

                result.append(sentence)
                if print_sentence:
                    print(sentence)

                count += 1

                if print_progress:
                    percentage = count * 100 / sentences_amount
                    if (percentage % 10) == 0:
                        print('%s%% (%s / %s)' % (percentage, count, sentences_amount))

                if count == sentences_amount:

                    if save_to_file:
                        save_sentences_to_file(result, file_name)

                    return result

        except (DisambiguationError, PageError):
            pass

    if save_to_file:
        save_sentences_to_file(result, file_name)

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


def save_sentences_to_file(lines, file_name):
    file = open(file_name, 'a')

    for x in lines:
        file.write('%s\n' % x)


if __name__ == '__main__':
    sentences = get_sentences_from_wiki(sentences_amount=500, print_sentence=False,
                                        save_to_file=True, file_name='sentences_from_wiki.txt',
                                        print_progress=True)
