import sys
import csv_parser.parser as parser
import stats.stats as stats

import ply.lex as lex

tokens = [
    'SC',  # START CODE
    'CONTENT',  # CONTENT
    'EC',  # END CODE
    'NEW_LINE',  # NEW LINE
]

states = (
    ('CODE', 'exclusive'),
)


def t_SC(t):
    r'{{'
    t.lexer.begin('CODE')


def t_CODE_CONTENT(t):
    r'[^}]+'
    variables = {}
    exec("var = " + t.value, globals(), variables)

    # Check the variable type and process the string acordingly
    if type(variables['var']) is dict:
        t.lexer.html += "<ul>"
        for key, val in variables['var'].items():
            t.lexer.html += "<li>" + t.lexer.dict_format.format(key=key, val=val) + "</li>\n"
        t.lexer.html += "</ul>"
    elif type(variables['var']) is list:
        t.lexer.html += "<ul>"
        for elem in variables['var']:
            t.lexer.html += "<li>" + t.lexer.list_format.format(elem=elem) + "</li>\n"
        t.lexer.html += "</ul>"
    else:
        t.lexer.html += variables['var']

    print('Found variable with name:', t.value)


def t_CODE_EC(t):
    r'}}'
    t.lexer.begin('INITIAL')


def t_CODE_error(t):
    print(f"Illegal character '{t.value[0]}' in line {t.lineno} in collumn {t.lexpos + 1}")
    sys.exit(2)


def t_EC(t):
    r'(.)'
    t.lexer.html += t.value
    # return t


def t_NEW_LINE(t):
    r'\n'
    t.lexer.html += t.value
    t.lexer.lineno += 1


# Função de erro
def t_error(t):
    print(f"ERROR")
    t.lexer.skip(1)  # Para continuar a analisar a string


# path -> html template path
# list_form -> how each element (elem) of the lists should be formatted
# dict_form -> how each element (key,value) of the dicts should be formatted
def parse_html(path, list_form, dict_form):
    # Analisador léxico
    lexer = lex.lex()
    lexer.html = ""

    # Save the formats into the lexer to be accessible to the token functions
    lexer.list_format = list_form
    lexer.dict_format = dict_form

    # Converting the html template into html

    with open(path, mode='r') as template:
        for line in template:
            lexer.input(line)
            for tok in lexer:
                pass

    with open("out.html", mode='w') as out:
        out.write(lexer.html)
