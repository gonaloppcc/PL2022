import ply.lex as lex
from checkLL1.look_ahead import look_ahead_main
from checkLL1.follow import follow

# Prints the n tabs
def print_tabs(n):
    s = ''
    for i in range(0, n):
        s += '\t'
    return s

# Prints the imports required to run the top down parser
def print_imports(lex_file):
    imports = 'import ply.yacc as yacc\n'
    imports += f'from {lex_file} import tokens, literals, lexer\n\n'

    return imports


# Prints the function that recognizes the non terminal simbol
# TODO: Improve code
def print_nterm(nterminal, terminals, literals):
    func = f'def rec_{nterminal[0]}():\n\tglobal next_simb\n'
    tab_num = 1
    for prop in nterminal[1].elements:
        first_simb = prop[0]
        if first_simb in literals:
            func += print_tabs(tab_num)
            func += f"if next_simb.type == {first_simb}:\n"
            tab_num += 1
            func += print_tabs(tab_num)
            func += f'rec_term({first_simb})\n'
        elif first_simb == 'empty':
            simbs = follow(nterminal[0], [])
            func += print_tabs(tab_num)
            func += f'if next_simb.type in {simbs}:\n'
            tab_num += 1
            func += print_tabs(tab_num)
            func += 'pass\n'
            tab_num -= 1
        elif first_simb in terminals.keys():
            func += print_tabs(tab_num)
            func += f"if next_simb.type == '{first_simb}':\n"
            tab_num += 1
            func += print_tabs(tab_num)
            func += f"rec_term('{first_simb}')\n"
        else:
            lookaheads = look_ahead_main(first_simb, [])
            func += print_tabs(tab_num)
            func += f'if next_simb.type in {lookaheads}:\n'
            tab_num += 1
            func += print_tabs(tab_num)
            func += f'rec_{first_simb}()\n'

        for i in range(1, len(prop)):
            func += print_tabs(tab_num)
            if prop[i] in literals:
                func += f'rec_term({prop[i]})\n'
            elif prop[i] in terminals.keys():
                func += f"rec_term('{prop[i]}')\n"
            else:
                func += f'rec_{prop[i]}()\n' 
 
        tab_num = 1
    func += print_tabs(tab_num)
    func += 'else:\n\t\tparse_error(next_simb)\n'
    func += '\n'
    return func


# Returns the function that parses errors
def print_parse_error():
    return '''
def parse_error(simb):
    print(f'Unknown symbol: {simb}')

'''


# Returns the function that recognizes terminal/literal simbols
def print_rec_term():
    return '''
def rec_term(simb):
    global next_simb
    if next_simb.type == simb:
        next_simb = lexer.token()
    else:
        parse_error(next_simb)
'''


# Returns the initialization of the next_simb global variable
def print_next_simb():
    return '''
next_simb = ('Error', '', 0, 0)
'''


# Main function of this module
# Prints the top down Python parser to a file
def make_top_down(nterminals, terminals, literals, lex_file, file):
    func = print_imports(lex_file)
    func += print_next_simb()
    func += print_rec_term()
    func += print_parse_error()
    for nterminal in nterminals.items():
        func += print_nterm(nterminal, terminals, literals)
    
    file.write(func)