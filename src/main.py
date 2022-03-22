from sys import argv

import stats.stats as stats
from website.template.template_to_html import parse_html


if __name__ == '__main__':
    csv = argv[1]
    template = argv[2]

    stats.get_stats(csv)
    parse_html(template, '<b>{elem[0]}</b>: {elem[1]}   -- {elem[2]}', '')
