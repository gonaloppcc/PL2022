import ply.yacc as yacc
from outputExpr_lex import tokens, literals, lexer


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
    if next_simb.type in ['num', 'id', 'pA']:
        rec_Exp()
        rec_term('$')
    else:
        parse_error(next_simb)

def rec_Exp():
    global next_simb
    if next_simb.type in ['num', 'id', 'pA']:
        rec_Termo()
        rec_Exp2()
    else:
        parse_error(next_simb)

def rec_Exp2():
    global next_simb
    if next_simb.type in ['$', 'pF']:
         pass
    elif next_simb.type == '+':
        rec_term('+')
        rec_Exp()
    elif next_simb.type == '-':
        rec_term('-')
        rec_Exp()
    else:
        parse_error(next_simb)

def rec_Termo():
    global next_simb
    if next_simb.type in ['num', 'id', 'pA']:
        rec_Fator()
        rec_Termo2()
    else:
        parse_error(next_simb)

def rec_Termo2():
    global next_simb
    if next_simb.type in ['$', '+', 'pF', '-']:
         pass
    elif next_simb.type == '*':
        rec_term('*')
        rec_Termo()
    elif next_simb.type == '/':
        rec_term('/')
        rec_Termo()
    else:
        parse_error(next_simb)

def rec_Fator():
    global next_simb
    if next_simb.type == 'num':
        rec_term('num')
    elif next_simb.type == 'id':
        rec_term('id')
    elif next_simb.type == 'pA':
        rec_term('pA')
        rec_Exp()
        rec_term('pF')
    else:
        parse_error(next_simb)

import outputExpr_top_down as td
import sys
for line in sys.stdin:
	lexer.input(line)
	td.next_simb = lexer.token()
	td.rec_S()
