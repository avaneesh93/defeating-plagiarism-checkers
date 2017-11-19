import language_check


def check(tool, data):
    matches = tool.check(data)
    print(len(matches))

    for i in range(0, len(matches)):
        print(matches[i].ruleId, matches[i].replacements)

    print(language_check.correct(data, matches))


if __name__ == '__main__':
    tool = language_check.LanguageTool('en-US')
    data = u'This is an wrong sentence. A sentence with a error in the Hitchhiker’s Guide tot he Galaxy'
    check(tool, data)

