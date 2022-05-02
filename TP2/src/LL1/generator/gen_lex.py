# Prints the tokens and their respective regex
# expressions in a function
#
# TODO: Add functions
def print_tokens(terminals, file):
    file.write('tokens = [ ')
    keys = list(terminals.keys())
    for i in range(0, len(keys)-1):
        file.write(f"'{keys[i]}', ")
    file.write(f"'{keys[len(keys)-1]}' ]\n\n")

    for simb in terminals.items():
        file.write(f'def t_{simb[0]}(t):\n')
        file.write(f"    r'{simb[1]}'\n\n")

# Prints the t_error function. Right now it just tells lex to
# skip to the next token.
#
# TODO: Add more functionality to errors
def print_error(file):
    file.write('def t_error(t):\n')
    file.write('    t.lexer.skip(1)\n\n')

# Prints the imports required to run the code
# In this case we only need ply.lex
def print_imports(file):
    file.write('import ply.lex as lex\n\n')

# Prints the lex.lex() function that initializes lex
def print_lex_start(file):
    file.write('lexer = lex.lex()\n')

# Main function to generate the full lex Python file
def make_lex(terminals, file):
    print_imports(file)
    print_tokens(terminals, file)
    print_error(file)
    print_lex_start(file)
