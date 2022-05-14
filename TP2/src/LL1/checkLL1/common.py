terminal_dic = {}
nterminal_dic = {}

debug = False


# Verifica se a expressão é terminal.
# Para isso, verifica se tem o símbolo ' ou é uma palavra associada a um símbolo terminal.
def is_terminal(expression):
    
    print("PRocura expression: ", expression)
    print("IN: ", terminal_dic)
    if "'" in expression or expression in terminal_dic.keys():
        return True
    else:
        return False


def is_empty(expression):
    if expression == "empty":
        return True
    else:
        return False
