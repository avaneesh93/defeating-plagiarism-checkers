from pos import set_parts_of_speech_in_tokens
from tokenize_paragraph import tokenize

PLAGIARISM_THRESHOLD = 60  # 60%
REPLACEMENTS_BEFORE_EACH_PLAGIARISM_CHECK = 2


def get_plagiarism_free_text(paragraph):
    all_tokens_of_all_sentences = tokenize(paragraph)


if __name__ == '__main__':
    text = open('./../datasets/test.txt', encoding='utf8').read()
    print(get_plagiarism_free_text(text))
