#!/usr/bin/env python3
import ply.lex as lex
import re
import sys
from checkLL1.rule import Rule
from checkLL1.common import is_terminal

states = [
            ('T', 'exclusive'), # Terminal, like num or id's simbols.
            ('NT', 'exclusive') # Nonterminal, like ABIN
        ]

tokens = [
    "TOKENS", # Start of the description of tokens.
    "NEW_TOKEN", # Description of one token.
    "NEW_N_TERMINAL", # Description of a new set of rules.
    "NEW_N_TERMINAL_RULE" # New rule associated with a previous Nonterminal simbol.
    ]

def t_ANY_error(t):
    t.lexer.skip(1)

# Read the beggining of the file.
def t_TOKENS(t):
    r'Tokens\:$'
    t.lexer.begin('T')

# Nesta situação assumimos que a expressão regex não tem espaços.
# Se tiver, temos de fazer doutra forma, mas não é difícil.
# Read one terminal simbol. They are described with the name and regex expression. 
def t_T_NEW_TOKEN(t):
    r'^([a-z]\w*)\s+(.+)$'
    separated = t.value.split(maxsplit=1)
    lexer.terminals[separated[0]] = separated[1]

# When the tokens part end in the original file.
# So, it starts to read non-terminal rules, and stores this rule name in the variable "lexer.last_nterminal_rule". 
def t_T_NEW_N_TERMINAL_RULE(t):
    r'^.*(?=:)'
    lexer.last_nterminal_rule = t.value
    t.lexer.begin('NT')

# Read a new set of rules related to one non-terminal simbol. 
# That non-terminal simbol is stored in the variable "lexer.last_nterminal_rule".
def t_NT_NEW_N_TERMINAL(t):
    r'^.*[^:](?=\n)' # Catch everything not ending in ':'
    elements = t.value.split()
    if lexer.last_nterminal_rule in lexer.nterminals :
        #lexer.nterminals[lexer.last_nterminal_rule].append(elements)
        lexer.nterminals[lexer.last_nterminal_rule].addElement(elements)
    else: 
        lexer.nterminals[lexer.last_nterminal_rule] = Rule([elements],None) # [elements]
    for element in elements:
        if is_terminal(element):
            lexer.tokens.append(element)

# Read a new rule name, and stores it in the variable "lexer.last_nterminal_rule".
def t_NT_NEW_N_TERMINAL_RULE(t):
    r'^.*(?=:)'
    lexer.last_nterminal_rule = t.value

t_ANY_ignore = " \n"

lexer = lex.lex()

# We decide to store the terminal carachters in a dictionary because we will search many times if a given simbol is terminal.
# The key of the terminals will be the name, and the key will be the value, wich is regex.
lexer.terminals = {}

'''
Here we store the non terminal information.
Will be stored this way:
Key: Rule name
Value: List of rules.
       Each rule is equivalent to one line of the file.
       Each individual rule is a list of elements. And each element has associated one flag.

Example file: 
Exp:
Exp '+' Termo
Termo

How we store:
Exp : 
    [
        [(Exp, 0) , ('+', 0) , (Termo, 0)],
        [(Termo, 0)]
    ]
'''
# Dictionaty to store the information related to non-terminal rules.
# The key is the rule name, and the values are the rules associated to the rule name.
lexer.nterminals = {}
lexer.last_nterminal_rule = ""
lexer.tokens = []

def file_reader(file : str):
    file1 = open(file, 'r')
    Lines = file1.readlines()
    
    for line in Lines:
        lexer.input(line)
        for tok in lexer:
            print(tok)
    return (lexer.terminals, lexer.nterminals, lexer.tokens )
