
terminal_dic = {}
nterminal_dic = {}

# Verifica se a expressão é terminal.
# Para isso, verifica se tem o símbolo ' ou é uma palavra associada a um símbolo terminal.
def is_terminal(expression):
    if "'" in expression or expression in terminal_dic.keys():
        print("É terminal: ", expression)
    else: 
        print("Não é terminal: ", expression)

# Aqui verificamos se uma entrada do dicionário de símbolos não terminais é válida ou não. 
# Para começar, se só tiver uma entrada não é necessário verificar.
def check_rule(rule_name, rules_list):
    # thing = ['Exp', "'$'"]
    for thing in  rules_list:
        for exp in thing:
            is_terminal(exp)

# Função principal que verifica se a liguagem descrita nos dois dicionários é LL(1)
# Recebe dois dicionários, no primeiro aparece o nome do símbolo terminal associado à expressão regex que o descreve.
# No segundo estão associados nomes de regras com as respetivas especificações.
# Por exemplo, "Exp -> Termo '+' num" é decrito como (Exp, [ [Termo, '+', num] ]).
def main_check_LL1(terminal_dic_rec, nterminal_dic_rec):
    global terminal_dic 
    terminal_dic = terminal_dic_rec
    global nterminal_dic 
    nterminal_dic = nterminal_dic_rec
    for rule_name, rules_list in nterminal_dic.items():
        check_rule(rule_name, rules_list)