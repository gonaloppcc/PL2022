import sys
import csv_parser.parser as parser
import stats.stats as stats

import ply.lex as lex

tokens = [
    'SC', # START CODE
    'EC', # END CODE
    'SNAME',  # START NAME
    'ENAME', # END NAME
    'SSTATS', # START STATS
    'ESTATS', # END STATS
    'SDATA', # START DATA
    'EDATA', # END DATA
    'CONTENT',  # CONTENT
    'NEW_LINE',  # NEW LINE
]

states = (
    ('CODE', 'exclusive'), # Code to be parsed
    ('NAME', 'exclusive'), # Print name
    ('STATS', 'exclusive'), # Print stats
    ('DATA', 'exclusive') # Print data
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
    r'name\['
    t.lexer.begin('NAME')

# Print name
def t_NAME_CONTENT(t):
    r'[a-zA-Z]\w+'
    t.lexer.html += t.lexer.module.statistics[t.value].get_name()

# End name state
def t_NAME_ENAME(t):
    r'\]'
    t.lexer.begin('CODE')


# Start stats state
def t_CODE_SSTATS(t):
    r'stats\['
    t.lexer.begin('STATS')

# Print the stats
def t_STATS_CONTENT(t):
    r'[a-zA-Z]\w+'
    t.lexer.html += t.lexer.module.statistics[t.value].print_stats()

# End stats state
def t_STATS_ESTATS(t):
    r'\]'
    t.lexer.begin('CODE')


# Start data state
def t_CODE_SDATA(t):
    r'data\['
    t.lexer.begin('DATA')

# Print the data
def t_DATA_CONTENT(t):
    r'[a-zA-Z]\w+'
    t.lexer.html += t.lexer.module.statistics[t.value].print_data()

# End data state
def t_DATA_EDATA(t):
    r'\]'
    t.lexer.begin('CODE')

# Any text outside the {{ }} will just get copied to the html
def t_CONTENT(t):
    r'.'
    t.lexer.html += t.value


def t_CODE_error(t):
    print(f"Illegal character '{t.value[0]}' in line {t.lineno} in collumn {t.lexpos + 1}")
    sys.exit(2)


def t_NEW_LINE(t):
    r'\n'
    t.lexer.html += t.value
    t.lexer.lineno += 1


# Função de erro
def t_error(t):
    print(f"ERROR")
    t.lexer.skip(1)  # Para continuar a analisar a string


# path -> html template path
# module -> Module containing the statistics
def parse_html(path, module):
    # Analisador léxico
    lexer = lex.lex()
    lexer.html = ""

    # Module where the stats are stored
    lexer.module = module

    # Converting the html template into html
    with open(path, mode='r') as template:
        for line in template:
            lexer.input(line)
            for tok in lexer:
                pass

    with open("out.html", mode='w') as out:
        out.write(lexer.html)
