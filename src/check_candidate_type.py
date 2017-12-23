CANDIDATE_POS_TYPES = ['JJ', 'JJR', 'JJS', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']
CANDIDATE_POS_TYPES_LOGREG = ['a', 's', 'v']


def is_candidate_pos_type(pos):
    return pos in CANDIDATE_POS_TYPES


def is_candidate_pos_type_log_reg(pos):
    return pos in CANDIDATE_POS_TYPES_LOGREG
