import os
from sys import argv

import stats.stats as stats
from website.template.template_to_html import parse_html


def write_list(var, depth):
    s = '<ul>'
    for elem in var:
        if type(elem) is dict:
            s += write_dict(var, depth)
        elif type(elem) is list:
            s += write_list(var, depth)
        else:
            s += f'<li><b>{elem[0]}</b>: {elem[1]}   -- {elem[2]}</li>\n'
    s += '</ul>'
    return s


def write_dict(var, depth):
    s = ''
    for key, value in var.items():
        s += '<h' + str(depth) + '>' + f'{key}' + '</h' + str(depth) + '>\n'
        if type(value) is dict:
            s += write_dict(value, depth + 1)
        elif type(value) is list:
            s += write_list(value, depth)
        else:
            s += str(value) + '\n'

    return s


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

    stats.get_stats(csv_path)
    parse_html(template_path, out_path, stats)
