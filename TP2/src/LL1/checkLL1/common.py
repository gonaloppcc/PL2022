terminal_dic = {}
nterminal_dic = {}
literals = []

debug = False


# Verifica se a expressão é terminal.
# Para isso, verifica se tem o símbolo ' ou é uma palavra associada a um símbolo terminal.
def is_terminal(expression):
    '''Checks if an expression is terminal.
        We choose to create a funcion in order to make changes int the definition of a terminal simbol easier .
        '''
    pairs_name_state = terminal_dic.keys()
    terminals = [pair[0] for pair in pairs_name_state]
    if expression in literals or expression in terminals:
        return True
    else:
        return False


def is_empty(expression):
    '''Here we define what is an empty expression.'''
    if expression == "empty":
        return True
    else:
        return False
