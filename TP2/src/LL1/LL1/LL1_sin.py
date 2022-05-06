# TODO: Define the syntax of the language

import ply.yacc as yacc
import sys
from LL1_lex import tokens, literals


def p_Grammar(p):
    "Grammar : TOKENS ':' NEW_LINE Tokens NonTerminalList"
    p[0] = (p[4], p[5])
    parser.ast = p[0]  # Abstract Syntax tree assigment


def p_Tokens_list(p):
    "Tokens : Tokens token NEW_LINE"
    p[1][p[2][0]] = p[2][1]
    p[0] = p[1]


def p_Tokens(p):
    "Tokens : empty"
    p[0] = {}


def p_NonTerminalList(p):  # Change this name to be not confused with *p_Tokens_list*
    "NonTerminalList : NonTerminalList NTerminal"
    p[1][p[2][0]] = p[2][1]
    p[0] = p[1]


def p_NonTerminal(p):
    "NonTerminalList : NTerminal"
    p[0] = {p[1][0]: p[1][1]}  # TODO: Change this to be more efficient


def p_NTerminal(p):
    "NTerminal : '-' NT ':' NEW_LINE Productions NEW_LINE"
    p[0] = (p[2], p[5])


def p_Productions_list(p):
    "Productions : Productions NEW_LINE Production"
    p[0] = p[1] + [p[3]]


def p_Productions(p):
    "Productions : Production"
    p[0] = [p[1]]


def p_Production_list(p):
    "Production : Production Simb"
    p[0] = p[1] + [p[2]]


def p_Production_simb(p):
    "Production : Simb"
    p[0] = [p[1]]


def p_Simb_empty(p):
    "Simb : EMPTY"
    p[0] = p[1]


def p_Simb_literal(p):
    "Simb : literal"
    p[0] = p[1]
    p.parser.literals.add(p[1])


def p_Simb_NT(p):
    "Simb : NT"
    p[0] = p[1]


def p_Simb_token(p):
    "Simb : token"
    p[0] = p[1]


# ------------------- Empty rule
def p_empty(p):
    'empty :'


# ---------------------- Handle Error function
def p_error(p):
    if not p:
        print('Unexpected end of input!')
    else:
        print('Syntax Error:', f'{p.value}', f'in line {p.lineno}.')
    parser.success = False


# ---------------------- Parser variables
parser = yacc.yacc(start='Grammar', debug=False, optimize=1)

parser.success = True

parser.literals = set()  # Set of all the literals found


# ----------------------- Analyzing the input
def ast_to_json(file_name: str, data):
    import json
    with open(file_name, 'w') as f:
        f.write(json.dumps(data))


content = sys.stdin.read()
parser.parse(content)
# TODO: Add arbitary new lines to the sintaxe
if parser.success:
    print('Correct sentence!')
    print('AST:', parser.ast)
    ast_to_json('ast.json', parser.ast)
    print('Literals:', parser.literals)
else:
    print('Invalid sentence!')
