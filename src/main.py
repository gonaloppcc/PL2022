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
    for key,value in var.items():        
        s += '<h' + str(depth) + '>' + f'{key}' + '</h' + str(depth) + '>\n'
        if type(value) is dict:
            s += write_dict(value, depth + 1)
        elif type(value) is list:
            s += write_list(value, depth)
        else:
            s += str(value) + '\n'

    return s

if __name__ == '__main__':
    if len(argv) != 4:
        print('Invalid number of arguments!', 'Please specify the emd file path and the template file path!', sep='\n')
        exit(2)

    else:
        csv = argv[1]
        template = argv[2]
        out_path = argv[3]

        stats.get_stats(csv)
        parse_html(template, out_path, stats)
