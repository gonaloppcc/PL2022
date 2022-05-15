# TODO: Define the tokens and the stuff
import ply.lex as lex
import logging

logging.basicConfig(level=20)

states = (
    # ('productions', 'exclusive') INITIAL STATE
    ('tokens', 'exclusive'),
    ('states', 'inclusive'),

    ('imports', 'exclusive'),  # Import state
)

literals = [':', '-']

tokens = [
    # Import state tokens
    'IMPORT',
    'path',

    # States
    'STATES',
    'incl',
    'excl',
    # Comment state related tokens
    'COMMENT',
    'MULTICOMMENT',  # Multiline comment
    #
    'NEW_LINE',
    'TOKENS',
    'EMPTY',
    'token',
    'name',
    'tokenState',
    'pop',
    'push',
    'expRegex',
    'NT',
    'literal',
]


# --- TODO: Add all keywords in the beginning of the file

# ---------------------------------------------- KEYWORDS --------------------------------------------------------------

# --------------------------------- State imports keywords
def t_IMPORT(t):
    r'[iI][mM][pP][oO][rR][tT]'
    t.lexer.begin('imports')
    return t


# --------------------------------- State state keywords
def t_STATES(t):
    r'[Ss][Tt][Aa][Tt][Ee][Ss]'
    t.lexer.begin('states')
    return t


def t_states_incl(t):
    r'incl'
    return t


def t_states_excl(t):
    r'excl'
    return t


def t_tokens_push(t):
    r'push\s*\(\w+\)'
    t.value = t.value.split('(', maxsplit=1)[1][:-1]
    return t


def t_tokens_pop(t):
    r'pop'
    return t


# --------------------------------- State Initial keywords
def t_EMPTY(t):
    r'[Ee][Mm][Pp][Tt][Yy]'
    return t


# --------------------------------- keywords of ANY state
def t_ANY_TOKENS(t: lex.Token):
    r'[Tt][Oo][Kk][Ee][Nn][Ss]'
    t.lexer.begin('tokens')
    return t


# ------------------------- Variable tokens -------------------------


# --------------------------------- End State state keywords

# --------------------------------- comments variable tokens
# Ignores the multiline comments
def t_MULTICOMMENT(t):
    r'\/\*(.|\n)*\*\/'
    t.lineno += t.value.count('\n')
    pass
    # No return value. Token discarded


# Ignores the one line comments
# noinspection PyUnusedLocal
def t_ANY_COMMENT(t):
    r'\#.*'
    pass
    # No return value. Token discarded


# TODO: Check order of tokens
# ------------------------- 'Tokens' state tokens
def t_tokens_tokenState(t):
    r'[a-z]\w*@[a-z]\w*'
    name, rexpr, *rest = t.value.split('@', maxsplit=1)  # TODO: Change this
    t.value = (name, rexpr)
    return t


def t_tokens_expRegex(t):
    r'\".+"'
    t.value = t.value[1:]
    t.value = t.value[:-1]
    return t


def t_tokens_token(t):
    r'[a-z]\w*'
    t.value = (t.value, "INITIAL")  # If no state is provided
    return t


# ----------------- 'Production'/ 'INITIAL' state tokens


def t_literal(t):
    r'\'.\''
    t.value = t.value[1]  # Removing the quotation marks
    return t


# -------------------------------- Import state variable tokens
def t_imports_path(t):
    r'\'[\w\./]+\''
    t.value = t.value[1:-1]
    return t


def t_imports_NEW_LINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)  # TODO: Fix Line number count
    t.lexer.begin('INITIAL')
    return t


# ------------------- Common tokens


def t_states_name(t):
    r'[a-z]\w*'
    return t


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
