# TODO: Define the syntax of the language

import ply.yacc as yacc
import sys

from typing import Dict

from LL1_lex import tokens, literals


def p_Grammar(p):
    "Grammar : Imports TokensBoiler NonTerminalList"
    p[0] = {
        'imports': p[1],
        'tokens': p[2],
        'literals': parser.literals,
        'non_terminals': p[3]
    }


def p_Imports(p):
    "Imports : empty"
    p[0] = []


def p_Imports_list(p):
    '''Imports : Imports Import
               | Imports Import NEW_LINE'''
    p[0] = p[1] + [p[2]]


def p_Import(p):
    "Import : IMPORT path"
    with open(p[2], 'r') as f:
        dict1 = lang_recon(f.read())
    p[0] = {
        'path': p[2],
        'ast': dict1
    }

    # TODO: Add semantic action to import action


def p_Tokens_boilerplate_empty(p):
    "TokensBoiler : empty"
    p[0] = {}


def p_Tokens_boilerplate(p):
    "TokensBoiler : TOKENS ':' NEW_LINE Tokens"
    p[0] = p[4]


def p_Tokens_list(p):
    '''Tokens : Tokens token
              | Tokens token NEW_LINE'''
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
    "NonTerminalList : empty"
    p[0] = {}  # TODO: Change this to be more efficient


def p_NTerminal(p):
    "NTerminal : '-' NT ':' NEW_LINE Productions"
    p[0] = (p[2], p[5])


def p_Productions(p):
    '''Productions : Production
                   | Production NEW_LINE'''
    p[0] = [p[1]]


def p_Productions_list(p):
    '''Productions : Productions Production
                   | Productions Production NEW_LINE'''
    p[0] = p[1] + [p[3]]


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
parser = yacc.yacc(start='Grammar', debug=False, optimize=0)

parser.success = True

parser.literals = set()  # Set of all the literals found TODO: Change this to be in the ast?


# ----------------------- Analyzing the input
def ast_to_json(file_name: str, data):
    import json
    with open(file_name, 'w') as f:
        f.write(json.dumps(data))


def lang_recon(text: str) -> dict:
    """
    Using the defined lang, this function recons a given text, returning the ast (Abstract Syntax Tree).
    """

    ast = parser.parse(text)
    # TODO: Add arbitary new lines to the sintaxe
    if parser.success:
        from tabulate import tabulate
        print('\t\t\t\t\tAST:\n', tabulate(ast, headers="keys"))
        for n_term, prod in ast['non_terminals'].items():
            print(f'{n_term}: ', prod)
    else:
        print('!!!Invalid input text!!!')

    return ast


lang_recon(sys.stdin.read())
