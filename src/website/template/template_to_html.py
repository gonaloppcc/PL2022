import sys

import ply.lex as lex

tokens = [
    'SC',  # START CODE
    'EC',  # END CODE
    'SNAME',  # START NAME
    'ENAME',  # END NAME
    'SSTATS',  # START STATS
    'ESTATS',  # END STATS
    'SDATA',  # START DATA
    'EDATA',  # END DATA
    'SLINK',  # START LINK
    'ELINK',  # END LINK
    'COMMA',  # COMMA
    'CONTENT',  # CONTENT
    'NEW_LINE',  # NEW LINE
]

states = (
    ('CODE', 'exclusive'),  # Code to be parsed
    ('NAME', 'exclusive'),  # Print name
    ('STATS', 'exclusive'),  # Print stats
    ('DATA', 'exclusive'),  # Print data
    ('LINKTEXT', 'exclusive'),  # Link text
    ('LINKLINK', 'exclusive')  # Link
)


# Start code state
def t_SC(t):
    r'{{'
    t.lexer.begin('CODE')


# End code state
def t_CODE_EC(t):
    r'}}'
    t.lexer.begin('INITIAL')


# Start name state
def t_CODE_SNAME(t):
    r'name\('
    t.lexer.begin('NAME')


# Print name
def t_NAME_CONTENT(t):
    r'[a-zA-Z]\w+'
    t.lexer.html += t.lexer.module.statistics[t.value].get_name()


# End name state
def t_NAME_ENAME(t):
    r'\)'
    t.lexer.begin('CODE')


# Start stats state
def t_CODE_SSTATS(t):
    r'stats\('
    t.lexer.begin('STATS')


# Print the stats
def t_STATS_CONTENT(t):
    r'[a-zA-Z]\w+'
    t.lexer.html += t.lexer.module.statistics[t.value].print_stats()


# End stats state
def t_STATS_ESTATS(t):
    r'\)'
    t.lexer.begin('CODE')


# Start data state
def t_CODE_SDATA(t):
    r'data\('
    t.lexer.begin('DATA')


# Print the data
def t_DATA_CONTENT(t):
    r'[a-zA-Z]\w+'
    t.lexer.html += t.lexer.module.statistics[t.value].print_data()


# End data state
def t_DATA_EDATA(t):
    r'\)'
    t.lexer.begin('CODE')


def t_CODE_SLINK(t):
    r'link\('
    t.lexer.begin('LINKTEXT')


def t_LINKTEXT_CONTENT(t):
    r'[^,)]+'
    t.lexer.templates.append({
        'text': t.value
    })


def t_LINKTEXT_COMMA(t):
    r','
    t.lexer.begin('LINKLINK')


def t_LINKLINK_CONTENT(t):
    r'[^,)]+'
    t.lexer.templates[-1]['link'] = t.value


def t_LINKLINK_ELINK(t):
    r'\)'
    template = t.lexer.templates[-1]
    link = t.lexer.templates[-1]['link'].split('.')[0] + '.html'
    text = t.lexer.templates[-1]['text']
    t.lexer.html += f'<a href="{link}">{text}</a>'
    t.lexer.begin('CODE')


t_CODE_ignore = '\t \n'
t_NAME_ignore = '\t \n'
t_STATS_ignore = '\t \n'
t_DATA_ignore = '\t \n'
t_LINKLINK_ignore = '\t \n'


# Any text outside the {{ }} will just get copied to the html
def t_CONTENT(t):
    r'.'
    t.lexer.html += t.value


def t_ANY_error(t):
    print(f"Illegal character '{t.value[0]}' in line {t.lineno} in collumn {t.lexpos + 1}")
    sys.exit(2)


def t_NEW_LINE(t):
    r'\n'
    t.lexer.html += t.value
    t.lexer.lineno += 1


# path -> html template path
# module -> Module containing the statistics
def parse_html(path, out_path, module):
    # Analisador léxico
    lexer = lex.lex()
    lexer.html = ""

    # Module where the stats are stored
    lexer.module = module
    lexer.templates = []

    # Converting the html template into html
    with open(path, mode='r') as template:
        for line in template:
            lexer.input(line)
            for tok in lexer:
                pass

    toks = path.split('/')
    file = toks[-1].split('.')[0] + '.html'
    folder = '/'.join(toks[0:-1])

    with open(out_path + '/' + file, mode='w', encoding='utf-8') as out:
        out.write(lexer.html)

    for template in lexer.templates:
        new_out_path = out_path + '/' + '/'.join(template['link'].split('/')[0:-1])

        parse_html(folder + '/' + template['link'], new_out_path, module)
