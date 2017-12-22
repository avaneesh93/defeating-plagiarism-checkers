import os

from tokenize_paragraph import tokenize

PLAGIARISM_THRESHOLD = 60  # 60%
REPLACEMENTS_BEFORE_EACH_PLAGIARISM_CHECK = 2


def get_plagiarism_free_text(paragraph):
    words = tokenize(paragraph)
    pass


if __name__ == '__main__':
    # Go to project root
    text = "Good writers accomplish these tasks by immediately establishing each paragraph’s topic and maintaining paragraph unity, by using concrete, personal examples to demonstrate their points, and by not prolonging the ending of the essay needlessly. Also, good writers study the target opportunity as carefully as they can, seeking to become an “insider,” perhaps even communicating with a professor they would like to work with at the target program, and tailoring the material accordingly so that evaluators can gauge the sincerity of their interest."
    print(get_plagiarism_free_text(text))
