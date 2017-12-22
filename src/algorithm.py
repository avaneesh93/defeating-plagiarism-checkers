from language_model_replacements import LanguageModelReplacement
from logistic_regression import LogReg
from output import generate_output_text_from_tokens
from set_best_replacement_word import set_best_replacement_word
from tokenize_input_text import tokenize

PLAGIARISM_THRESHOLD = 60  # 60%
REPLACEMENTS_BEFORE_EACH_PLAGIARISM_CHECK = 2


def get_plagiarism_free_text(input_text):
    all_tokens_of_all_sentences = tokenize(input_text)
    LogReg().set_replacements_in_tokens(all_tokens_of_all_sentences)
    LanguageModelReplacement().set_language_model_replacements(all_tokens_of_all_sentences)
    # TODO Add synonym API as well?
    set_best_replacement_word(all_tokens_of_all_sentences)
    return generate_output_text_from_tokens(all_tokens_of_all_sentences)


if __name__ == '__main__':
    input_text = open('./../datasets/input_text.txt', encoding='utf8').read()
    print(get_plagiarism_free_text(input_text))
