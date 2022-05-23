import ply.yacc as yacc
from outputStates_lex import tokens, literals, lexer


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
    if next_simb.type in ['palavra', '$', 'iniNumState']:
        rec_Coisas()
        rec_term('$')
    else:
        parse_error(next_simb)

def rec_Coisas():
    global next_simb
    if next_simb.type in ['palavra', '$', 'iniNumState']:
        rec_ListaPalavra()
        rec_ListaNumState()
    else:
        parse_error(next_simb)

def rec_ListaPalavra():
    global next_simb
    if next_simb.type == 'palavra':
        rec_term('palavra')
        rec_ListaPalavra()
    elif next_simb.type in ['$', 'iniNumState']:
         pass
    else:
        parse_error(next_simb)

def rec_ListaNumState():
    global next_simb
    if next_simb.type == 'iniNumState':
        rec_term('iniNumState')
        rec_ListaNum()
        rec_term('fim')
    elif next_simb.type in ['$']:
         pass
    else:
        parse_error(next_simb)

def rec_ListaNum():
    global next_simb
    if next_simb.type == 'num':
        rec_term('num')
        rec_ListaNum()
    elif next_simb.type in ['fim']:
         pass
    else:
        parse_error(next_simb)

import outputStates_top_down as td
import sys
for line in sys.stdin:
	lexer.input(line)
	td.next_simb = lexer.token()
	td.rec_S()
