import ply.yacc as yacc
from parentesis/output_lex import tokens, literals, lexer


next_simb = ('Error', '', 0, 0)

def rec_term(simb):
    global next_simb
    if next_simb.type == simb:
        next_simb = lexer.token()
    else:
        parse_error(next_simb)

def parse_error(simb):
    print(f'Unknown symbol: {simb}')

def rec_S():
    global next_simb
    if next_simb.type in ['pA', '$', 'pF']:
        rec_S1()
        rec_term('$')
    else:
        parse_error(next_simb)

def rec_S1():
    global next_simb
    if next_simb.type == 'pA':
        rec_term('pA')
        rec_S1()
        rec_term('pF')
        rec_S1()
    elif next_simb.type in ['$', 'pF']:
         pass
    else:
        parse_error(next_simb)


import output_top_down as td

import sys
for line in sys.stdin:
    lexer.input(line)
    td.next_simb = lexer.token()
    td.rec_S()
    