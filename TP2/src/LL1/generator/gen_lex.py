# Prints the tokens and their respective regex
# expressions in a function
#
# TODO: Add functions
def print_tokens(terminals, file):
    file.write('tokens = [')
    keys = list(terminals.keys())
    if len(keys) > 0:
        for i in range(0, len(keys) - 1):
            file.write(f"'{keys[i][0]}', ")
        file.write(f"'{keys[len(keys) - 1][0]}'")
    file.write(']\n\n')

    for simb in terminals.items():
        if simb[0][0] == 'ignore':
            file.write(f"t_{simb[0][1]}_ignore = '{simb[1]['regex']}'\n\n")
        else:
            file.write(f'def t_{simb[0][1]}_{simb[0][0]}(t):\n')
            file.write(f"    r'{simb[1]['regex']}'\n")
            if simb[1]['func'] is not None:
                if simb[1]['func'][0] == 'push':
                    print_push(simb[1]['func'][1], file)
                elif simb[1]['func'][0] == 'pop':
                    print_pop(file)
            file.write(f"    return t\n\n")


def print_states(states, file):
    file.write('states = [')
    items = list(states.items())
    if len(items) > 0:
        for i in range(0, len(items) - 1):
            file.write(f"('{items[i][0]}',")
            if items[i][1] == 'incl':
                file.write("'inclusive'), ")
            else:
                file.write("'exclusive'), ")
        file.write(f"('{items[len(items) - 1][0]}',")
        if items[len(items) - 1][1] == 'incl':
            file.write("'inclusive') ")
        else:
            file.write("'exclusive') ")
    file.write(']\n\n')


# Prints the terminals list to the lex file
def print_literals(literals, file):
    file.write('literals = [')
    list_l = list(literals)
    if len(literals) != 0:
        for i in range(0, len(list_l) - 1):
            file.write(f"'{list_l[i]}',")
        file.write(f" '{list_l[len(list_l) - 1]}'")
    file.write(f"]\n\n")


# Prints the t_error function. Right now it just tells lex to
# skip to the next token.
#
# TODO: Add more functionality to errors
def print_error(file):
    file.write('def t_error(t):\n')
    file.write('    t.lexer.skip(1)\n')
    file.write('    return t\n\n')


# Prints the imports required to run the code
# In this case we only need ply.lex
def print_imports(file):
    file.write('import ply.lex as lex\n\n')


def print_push(state, file):
    file.write(f"    t.lexer.push_state('{state}')\n")


def print_pop(file):
    file.write('    t.lexer.pop_state()\n')


# Prints the lex.lex() function that initializes lex
def print_lex_start(file):
    file.write('lexer = lex.lex()\n')


# Main function to generate the full lex Python file
def make_lex(states, terminals, literals, file):
    print_imports(file)
    print_states(states, file)
    print_literals(literals, file)
    print_tokens(terminals, file)
    print_error(file)
    print_lex_start(file)
