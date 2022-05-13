# TODO: Define the tokens and the stuff
import ply.lex as lex

states = (
    # ('productions', 'exclusive') INITIAL STATE
    ('tokens', 'exclusive'),
    #('states1', 'inclusive'),
)

literals = [':', '-']

tokens = [
    'NEW_LINE',
    'TOKENS',
    'EMPTY',
    'token',
    'NT',
    'literal',
    #'import',
    'state',
    'incl',
    'excl',
    'name',
    'tokenState',
    'expRegex'
]
# ------------------- State tokens

def t_state(t):
    r'states'
    return t

def t_incl(t):
    r'incl'
    return t

def t_excl(t):
    r'excl'
    return t

def t_name(t):
    r'[a-z]\w*'
    return t
# --------- End State definition



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



'''
def t_tokens_token2(t):
    r'[a-z]\w*\s+.+'  # num \d+
    name, rexpr, *rest = t.value.split(' ', maxsplit=1)  # TODO: Change this
    t.value = (name, rexpr)
    return t
'''
def t_tokens_tokenState (t):
    r'[a-z]\w*@[a-z]\w*'
    if t.lexer.regex:
        t.lexer.regex = True
    name, rexpr, *rest = t.value.split('@', maxsplit=1)  # TODO: Change this
    t.value = (name, rexpr)
    print("Leu tokenState: ", t.value)
    return 

def t_tokens_token(t):
    r'[a-z]\w*'
    print("Leu token: ", t.value)
    return t


# ----------------- 'Production'/ 'INITIAL' state tokens
def t_EMPTY(t):
    r'empty'  # TODO: Convert to case insensitive
    return t


def t_TOKENS(t: lex.Token):
    r'Tokens'  # TODO: Convert to case insensitive
    #if t.lexer.states:
    #    t.lexer.pop_state()
     #   t.lexer.states = False
    t.lexer.begin('tokens')
    return t


def t_literal(t):
    r'\'.\''
    t.value = t.value[1]  # Removing the quotation marks
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
    if t.lexer.regex:
        t.lexer.regex = False
        t.lexer.pop_state()
    t.lexer.begin('INITIAL')
    return t

def t_ANY_NEW_LINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)  # TODO: Fix Line number count
    return t


t_ANY_ignore = ' \t'


def t_ANY_error(t):
    print("Illegal character,", f'{t.value[0]}', f'in line {t.lineno}.')
    print(t)
    print(t.lexer.states)
    print('Input is invalid!!!')
    exit(1)  # Exit code of an invalid recognition

    # A expressão regex não pode ter ' '?

def t_tokens_expRegex(t):
    r'[^\-@\n]+'
    print("Leu expRegex: ", t.value)
    return t




# --------- End Token definition


lexer = lex.lex()

# ------------ Lexer state definition
lexer.lineno = 1

lexer.collumn = 1  # TODO: Is this need?

# Necessary to know if there is need for a pop state after states.
lexer.states = False  
lexer.regex = False  

# ----------------------- Testing

if __name__ == '__main__':
    import sys

    content = sys.stdin.read()
    lexer.input(content)

    for tok in lexer:
        # print(tok.value, '', end='')
        print(tok)
