import ply.yacc as yacc
from output_lex import tokens, literals, lexer


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
    if next_simb.type == 'pA':
        rec_term('pA')
        rec_S()
        rec_pF()
    else:
        parse_error(next_simb)

