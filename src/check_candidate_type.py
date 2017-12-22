CANDIDATE_POS_TYPES = ['ADJ']
CANDIDATE_POS_TYPES_LOGREG = ['a']


def is_candidate_type(pos):
    return pos in CANDIDATE_POS_TYPES


def is_candidate_type_log_reg(pos):
    return pos in CANDIDATE_POS_TYPES_LOGREG
