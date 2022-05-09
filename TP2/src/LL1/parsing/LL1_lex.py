# TODO: Define the tokens and the stuff
import ply.lex as lex

states = (
    # ('productions', 'exclusive') INITIAL STATE
    ('tokens', 'exclusive'),
)

literals = [':', '-']

tokens = [
    'NEW_LINE',
    'TOKENS',
    'EMPTY',
    'token',
    'NT',
    'literal',
    'import'
]


# TODO: Check order of tokens

# --------------- Comments
def t_ANY_COMMENT_MULTILINE(t):
    r'\/\*(.|\n)*\*\/(\n*)'
    print('Comment:', f'\'{t.value}\'')  # TODO: Debug purposes
    t.lexer.lineno += t.value.count('\n')
    pass


def t_ANY_COMMENT(t):
    r'\#.*\n*'
    print('Comment:', f'\'{t.value}\'')  # TODO: Debug purposes
    t.lexer.lineno += t.value.count('\n')
    pass


# ------------------------- 'Tokens' state tokens
def t_tokens_token(t):
    r'[a-z]\w*\s+.+'  # num \d+
    name, rexpr, *rest = t.value.split(' ')  # TODO: Change this
    t.value = (name, rexpr)
    return t


# ----------------- 'Production'/ 'INITIAL' state tokens
def t_EMPTY(t):
    r'empty'  # TODO: Convert to case insensitive
    return t


def t_TOKENS(t: lex.Token):
    r'Tokens'  # TODO: Convert to case insensitive
    t.lexer.begin('tokens')
    return t


def t_literal(t):
    r'\'.\''
    # t.value = t.value[1]  # Removing the quotation marks
    return t


# ------------------- Common tokens
def t_ANY_import(t):
    r'import'
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
    print("Illegal character,", f'{t.value[0]}', f'in line {t.lineno}.')
    print('Input is invalid!!!')
    exit(1)  # Exit code of an invalid recognition


# --------- End Token definition

lexer = lex.lex()

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
