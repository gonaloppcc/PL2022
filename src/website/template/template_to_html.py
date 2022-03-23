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

    var = variables['var']
    if type(var) is dict:
        t.lexer.html += t.lexer.dict_func(var, 1)
    elif type(var) is list:
        t.lexer.html += t.lexer.list_func(var, 1)
    else:
        t.lexer.html += str(var)

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
# list_func -> Function that turns a list into string
# dict_form -> Function that turns a dict into string
def parse_html(path, list_func, dict_func):
    # Analisador léxico
    lexer = lex.lex()
    lexer.html = ""

    # Save the formats into the lexer to be accessible to the token functions
    lexer.list_func = list_func
    lexer.dict_func = dict_func

    # Converting the html template into html

    with open(path, mode='r') as template:
        for line in template:
            lexer.input(line)
            for tok in lexer:
                pass

    with open("out.html", mode='w') as out:
        out.write(lexer.html)
