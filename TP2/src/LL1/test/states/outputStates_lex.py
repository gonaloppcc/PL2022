import ply.lex as lex

states = [('numState','inclusive') ]

literals = [ '$']

tokens = ['num', 'fim', 'palavra', 'iniNumState', 'ignore']

def t_numState_num(t):
    r'\d+'
    return t

def t_numState_fim(t):
    r'\)'
    t.lexer.pop_state()
    return t

def t_INITIAL_palavra(t):
    r'\w+'
    return t

def t_INITIAL_iniNumState(t):
    r'\('
    t.lexer.push_state('numState')
    return t

t_INITIAL_ignore = '\t \n'

def t_error(t):
    t.lexer.skip(1)
    return t

lexer = lex.lex()
