import sys
import csv_parser.parser as parser

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
    r'\w+'
    variables = {}
    exec("var = " + t.value, globals(), variables)
    t.lexer.html += str(variables['var'])
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


# Analisador léxico
lexer = lex.lex()
lexer.html = ""

# Load the data from the dataset
exams = parser.parse_emd('../../files/emd.csv')

# Converting the html template into html

for line in sys.stdin:
    lexer.input(line)
    for tok in lexer:
        print(tok)

print("Html", lexer.html)
