terminal_dic = {}
nterminal_dic = {}

debug = True


# Verifica se a expressão é terminal.
# Para isso, verifica se tem o símbolo ' ou é uma palavra associada a um símbolo terminal.
def is_terminal(expression):
    if "'" in expression or expression in terminal_dic.keys():
        return True
        # print("É terminal: ", expression)
    else:
        # print("Não é terminal: ", expression)
        return False


def is_empty(expression):
    if expression == "empty":
        return True
    else:
        return False
