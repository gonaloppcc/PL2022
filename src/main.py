from sys import argv

import stats.stats as stats
from website.template.template_to_html import parse_html


if __name__ == '__main__':
    if len(argv) != 3:
        print('Invalid number of arguments!', 'Please specify the emd file path and the template file path!', sep='\n')
        exit(2)

    else:
        csv = argv[1]
        template = argv[2]

        stats.get_stats(csv)
        parse_html(template, '<b>{elem[0]}</b>: {elem[1]}   -- {elem[2]}', '')
