# TODO: Define the syntax of the language

import ply.yacc as yacc
import sys
from LL1_lex import tokens, literals


def p_Grammar(p):
    "Grammar : TOKENS ':' NEW_LINE Tokens NEW_LINE Productions"
    x = 0
    y = 2
    p[0] = y


def p_Tokens_list(p):
    "Tokens : Tokens token NEW_LINE"


def p_Tokens(p):
    "Tokens : empty"


def p_Productions_list(p):
    "Productions : Productions NT_productions"


def p_Productions(p):
    # "Productions : NT_productions"
    "Productions :"


def p_NT_productions(p):
    "NT_productions : NT ':' NEW_LINE Rules NEW_LINE"


def p_Rules_list(p):
    "Rules : Rules NEW_LINE Conj_simb"


def p_Rules(p):
    "Rules : Conj_simb"


def p_Conj_simb_list(p):
    "Conj_simb : Conj_simb Simb"


def p_Conj_simb(p):
    "Conj_simb : Simb"


def p_Simb_empty(p):
    "Simb : EMPTY"


def p_Simb_literal(p):
    "Simb : literal"


def p_Simb_NT(p):
    "Simb : NT"


def p_Simb_token(p):
    "Simb : token"


# ------------------- Empty rule
def p_empty(p):
    'empty :'


# ---------------------- Handle Error function
def p_error(p):
    print('Sintaxe error:', p)
    parser.success = False


# ---------------------- Parser variables
parser = yacc.yacc(start='Grammar')

parser.success = True

parser.terminals = {}  # Dict of the terminal symbols of the language

# TODO: Finish this
parser.current_non_terminal = ""  # Current non-terminal from which the productions belong

parser.literals = []  # List of the literals used

parser.non_terminals = {}  # Dict of the non-terminal symbols and their productions

# ----------------------- Analyzing the input

content = sys.stdin.read()
parser.parse(content)
# TODO: Add arbitary new lines to the sintaxe
if parser.success:
    print("Correct sentence!")
    # print("Correct sentence:", content)
else:
    print("Invalid sentence!")
    # print("Invalid sentence:", content)
