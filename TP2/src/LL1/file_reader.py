#!/usr/bin/env python3
import ply.lex as lex
import re
import sys

states = [
            ('T', 'exclusive'), # Terminal, tipo num
            ('NT', 'exclusive') # Nonterminal, tipo ABIN
        ]

tokens = ["TOKENS","NEW_TOKEN","NEW_N_TERMINAL", "NEW_N_TERMINAL_RULE"]

def t_ANY_error(t):
    t.lexer.skip(1)

def t_TOKENS(t):
    r'Tokens\:$'
    t.lexer.begin('T')

# Nesta situação assumimos que a expressão regex não tem espaços.
# Se tiver, temos de fazer doutra forma, mas não é difícil.
def t_T_NEW_TOKEN(t):
    r'^([a-z]\w*)\s+([\[\]\+\*\\a-zA-Z_-]+)$'
    separated = t.value.split()
    lexer.terminals[separated[0]] = separated[1]

def t_T_NEW_N_TERMINAL_RULE(t):
    r'^.*(?=:)'
    lexer.last_nterminal_rule = t.value
    t.lexer.begin('NT')

def t_NT_NEW_N_TERMINAL(t):
    r'^.*[^:](?=\n)' #Catch everything not ending in ':'
    if lexer.last_nterminal_rule in lexer.nterminals :
        lexer.nterminals[lexer.last_nterminal_rule].append(t.value)
    else: 
        lexer.nterminals[lexer.last_nterminal_rule] = [t.value]

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
lexer.nterminals = {}
lexer.last_nterminal_rule = ""


file1 = open('input.txt', 'r')
Lines = file1.readlines()
 
# Strips the newline character
for line in Lines:
    lexer.input(line)
    for tok in lexer:
        print(tok)

print("Terminais:")
for key, value in lexer.terminals.items():
    print(f"Key: {key} | Value: {value}")

print("Não Terminais:")
for key, value in lexer.nterminals.items():
    for rule in value:
        print(f"Key: {key} | One rule: {rule}")