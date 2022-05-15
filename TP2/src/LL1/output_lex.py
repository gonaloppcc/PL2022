import ply.lex as lex

tokens = [ '('pA', 'INITIAL')', '('pF', 'INITIAL')' ]

def t_('pA', 'INITIAL')(t):
    r'{'name': ('pA', 'INITIAL'), 'regex': '(', 'func': None}'
    return t

def t_('pF', 'INITIAL')(t):
    r'{'name': ('pF', 'INITIAL'), 'regex': ')', 'func': None}'
    return t

def t_error(t):
    t.lexer.skip(1)

lexer = lex.lex()
