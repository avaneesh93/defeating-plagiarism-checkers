import language_check


def repair_grammar(text, tool=language_check.LanguageTool('en-US')):
    matches = tool.check(text)
    print(len(matches))

    for i in range(0, len(matches)):
        print(matches[i].ruleId, matches[i].replacements)

    return language_check.correct(text, matches)


if __name__ == '__main__':
    data = 'This is an wrong sentence. A sentence with a error in the Hitchhiker’s Guide tot he Galaxy'
    print(repair_grammar(data))
