import ply.lex as lex

tokens = [
    'tokens',
    'new_token',
    'terminal',
    'n_terminal',
    'literal',

    'def_n_terminal'
]

t_terminal = r'[a-z]\w+'
t_n_terminal = r'[A-Z]\w+'
t_literal = r"'.'"

t_ignore = ' \t\n'

states = (
    ('T', 'exclusive'),  # Terminal
    ('NT', 'exclusive')  # Nonterminal
)


# INITIAL STATE

def t_INITIAL_tokens(t):
    r'Tokens\:$'
    t.lexer.begin('T')


# TERMINAL STATE

def t_T_new_token(t):
    r"[a-z]\w+ .*"
    # TODO: Add to the dictinary the new token


def t_error(t):
    print("Caracter ilegal, ", t.value[0])
    t.lexer.skip(1)


lex.lex()
