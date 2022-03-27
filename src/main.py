import os
from sys import argv

import stats.stats as stats
from csv_parser.parser import parse_emd
from website.template.template_to_html import parse_html

if __name__ == '__main__':
    out_path = 'out'  # Default output folder
    if len(argv) == 4:
        out_path = argv[3]

    elif len(argv) == 3:  # No optional argument provided
        pass

    else:
        print('Invalid number of arguments!', 'Please specify the emd file path and the template file path!',
              'Optionaly you can provide the name of output path.', sep='\n')
        exit(2)

    csv_path = argv[1]
    template_path = argv[2]

    if not os.path.isfile(csv_path):
        print('Invalid csv file path!')
        exit(2)

    if not os.path.isfile(template_path):
        print('Invalid template file path!')
        exit(2)

    if not os.path.exists(out_path):  # Creates the output folder if it does not exist
        os.mkdir(out_path)

    csv = parse_emd(csv_path)
    print('Data loaded!')

    statistics = stats.get_stats(csv)
    parse_html(template_path, out_path, statistics)
