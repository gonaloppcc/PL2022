terminal_dic = {}
nterminal_dic = {}

debug = True


# Verifica se a expressão é terminal.
# Para isso, verifica se tem o símbolo ' ou é uma palavra associada a um símbolo terminal.
def is_terminal(expression):
    pairs_name_state = terminal_dic.keys()
    terminals = [pair[0] for pair in pairs_name_state]
    if "'" in expression or expression in terminals:
        return True
    else:
        return False


def is_empty(expression):
    if expression == "empty":
        return True
    else:
        return False
