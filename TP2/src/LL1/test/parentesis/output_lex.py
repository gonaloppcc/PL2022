import ply.lex as lex

states = []

literals = [ '$']

tokens = ['pA', 'pF', 'ignore']

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
