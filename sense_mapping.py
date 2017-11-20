def parse_sense_mapping(filename):
    sense_map = {}
    with open(filename, 'r') as f:
        lines = f.readlines()

    for line in lines:
        senses = line.split('\t')
        wordnet_senses = senses[1].strip().split(',')

        sense_map[senses[0]] = wordnet_senses
    return sense_map
