from checkLL1 import follow, look_ahead


# Prints the imports required to run the top down parser
def print_imports(lex_file, file):
    imports = 'import ply.yacc as yacc\n'
    imports += f'from {lex_file} import tokens, literals, lexer\n\n'

    file.write(imports)


# Prints the function that recognizes the non terminal simbol
# TODO: Improve code
def print_nterm(nterminal, terminals, literals, file):
    func = f'def rec_{nterminal[0]}():\n'
    func += f'    global next_simb\n'

    first = True
    for prop in nterminal[1]:
        first_simb = prop[0]

        if not first:
            func += '    el'  # If it's not the first proposition write elif
        else:
            func += '    '  # If it's the first proposition write if and set first to False
            first = False

        if first_simb == 'empty':
            simbs = follow(nterminal[0], [])
            func += f'if next_simb.type in {simbs}:\n'
            func += '         pass\n'
        elif first_simb in literals or first_simb in terminals.keys():
            func += f"if next_simb.type == '{first_simb}':\n"
            func += f"        rec_term('{first_simb}')\n"
        else:
            lookaheads = look_ahead_main(first_simb, [])
            func += f'if next_simb.type in {lookaheads}:\n'
            func += f'        rec_{first_simb}()\n'

        for i in range(1, len(prop)):
            if prop[i] in literals or prop[i] in terminals.keys():
                func += f"        rec_term('{prop[i]}')\n"
            else:
                func += f'        rec_{prop[i]}()\n'

    func += '    else:\n'
    func += '        parse_error(next_simb)\n\n'
    file.write(func)


# Returns the function that parses errors
def print_parse_error(file):
    func = '''
def parse_error(simb):
    print(f'Unknown symbol: {simb}')

'''
    file.write(func)


# Returns the function that recognizes terminal/literal simbols
def print_rec_term(file):
    func = '''
def rec_term(simb):
    global next_simb
    if next_simb.type == simb:
        next_simb = lexer.token()
    else:
        parse_error(next_simb)
'''
    file.write(func)


# Returns the initialization of the next_simb global variable
def print_next_simb(file):
    simb = '''
next_simb = ('Error', '', 0, 0)
'''
    file.write(simb)


# Main function of this module
# Prints the top down Python parser to a file
def make_top_down(nterminals, terminals, literals, lex_file, file):
    print_imports(lex_file, file)
    print_next_simb(file)
    print_rec_term(file)
    print_parse_error(file)
    for nterminal in nterminals.items():
        print_nterm(nterminal, terminals, literals, file)
