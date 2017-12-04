import time

from copyleaks.copyleakscloud import CopyleaksCloud
from copyleaks.product import Product


def detect_plagiarism(text):
    cloud = CopyleaksCloud(Product.Education, 'dakshjay@gmail.com',
                           '28C777CE-12BF-4132-97DC-60BD198D618F')
    process = cloud.createByText(text)

    print('Checking for Plagiarism...')
    is_completed = False
    while not is_completed:
        # Get process status
        [is_completed, percents] = process.isCompleted()
        print('%s%s%s%%' % ('#' * int(percents / 2), "-" * (50 - int(percents / 2)), percents))
        if not is_completed:
            time.sleep(2)

    print('Process Finished!')

    # for result in process.getResutls():
    #     print('Percent = %s%%' % result.getPercents())
    #     print('Comparison Report = %s' % result.getComparisonReport())
    #     print('Title = %s' % result.getTitle())
    #     print('Introduction = %s' % result.getIntroduction())

    max_plagiarism_percentage = 0

    if len(process.getResutls()) > 0:
        max_plagiarism_percentage = \
            sorted(process.getResutls(), key=lambda x: x.getPercents(), reverse=True)[
                0].getPercents()

    print('%s%% Plagiarism Detected.' % max_plagiarism_percentage)


if __name__ == '__main__':
    # text = 'The ecological restoration of islands, or island restoration, is the application of the principles of ecological restoration to islands and island groups.'
    text = 'The ecological rehabilitation of islands, or island rehabilitation, is the implementation of the rules of ecological rehabilitation to islands and island groups.'
    detect_plagiarism(text)
