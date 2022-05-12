# TODO: Define the tokens and the stuff
import ply.lex as lex
import logging

logging.basicConfig(level=20)

states = (
    # ('productions', 'exclusive') INITIAL STATE
    ('tokens', 'exclusive'),

    ('commentsLine', 'exclusive'),
    ('commentsMultiline', 'exclusive'),

    ('imports', 'exclusive'),  # Import state
)

literals = [':', '-']

tokens = [
    # Import state tokens
    'IMPORT',
    'path',  # TODO: Maybe add a *ALIAS* option

    # Comment state related tokens
    'BCOMLINE',  # Begin one line comment
    'ECOMLINE',  # End one line comment
    'txt',  # Ignore everything inside a comment
    'BCOM',  # Begin multi line comment
    'ECOM',  # End multi line comment
    #
    'NEW_LINE',
    'TOKENS',
    'EMPTY',
    'token',
    'NT',
    'literal',
]


# TODO: Check order of tokens
# ------------------------- 'Tokens' state tokens
def t_tokens_token(t):
    r'[a-z]\w*\s+.+'  # num \d+
    name, rexpr, *rest = t.value.split(' ', maxsplit=1)  # TODO: Change this
    t.value = (name, rexpr)
    return t


# ----------------- 'Production'/ 'INITIAL' state tokens
def t_EMPTY(t):
    r'[Ee][Mm][Pp][Tt][Yy]'
    return t


def t_TOKENS(t: lex.Token):
    r'[Tt][Oo][Kk][Ee][Nn][Ss]'
    t.lexer.begin('tokens')
    return t


def t_literal(t):
    r'\'.\''
    t.value = t.value[1]  # Removing the quotation marks
    return t


def t_IMPORT(t):
    r'[iI][mM][pP][oO][rR][tT]'
    t.lexer.begin('imports')
    return t


# -------------------------------- Import state tokens
def t_imports_path(t):
    r'\'[\w\.]+\''
    t.value = t.value[1:-1]
    return t


def t_imports_NEW_LINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)  # TODO: Fix Line number count
    t.lexer.begin('INITIAL')
    return t


# ------------------- Common tokens


def t_ANY_token(t):
    r'[a-z]\w*'
    return t


def t_ANY_NT(t):
    r'[A-Z]\w*'
    t.lexer.begin('INITIAL')
    return t


def t_ANY_NEW_LINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)  # TODO: Fix Line number count
    return t


t_ANY_ignore = ' \t'


def t_ANY_error(t):
    print("Illegal character,", f'{repr(t.value[0])}', f'in line {t.lineno}.')
    print('!!! Input is invalid !!!')
    exit(1)  # Exit code of an invalid recognition


# --------- End Token definition

lexer = lex.lex(debug=False)

# ------------ Lexer state definition
lexer.lineno = 1

lexer.collumn = 1  # TODO: Is this need?

# ----------------------- Testing

if __name__ == '__main__':
    import sys

    content = sys.stdin.read()
    lexer.input(content)

    for tok in lexer:
        # print(tok.value, '', end='')
        print(tok)
