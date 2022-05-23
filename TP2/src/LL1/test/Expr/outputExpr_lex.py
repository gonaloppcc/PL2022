import ply.lex as lex

states = []

literals = ['*','-','/','$', '+']

tokens = ['num', 'id', 'name', 'pA', 'pF', 'ignore']

def t_INITIAL_num(t):
    r'\d+'
    return t

def t_INITIAL_id(t):
    r'[a-zA-Z_]\w*'
    return t

def t_INITIAL_name(t):
    r'\w+'
    return t

def t_INITIAL_pA(t):
    r'\('
    return t

def t_INITIAL_pF(t):
    r'\)'
    return t

t_INITIAL_ignore = '\t \n'

def t_error(t):
    t.lexer.skip(1)
    return t

lexer = lex.lex()
