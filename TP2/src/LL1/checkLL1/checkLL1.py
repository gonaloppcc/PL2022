from checkLL1.follow import follow
from checkLL1.look_ahead import look_ahead_main
# from checkLL1.common import terminal_dic, nterminal_dic, is_terminal
import checkLL1.common as common

'''
Notas para testes
Meter palavras que não existem.
Meter nomes de símbolos terminais que não são descritos a seguir
Meter S: A \n A: S
Com o mesmo símbolo terminal

Notas:
Quando à frente de uma expressão tem um espaço, ele não lê, do tipo:
"Termo2: "
Também não lê a última linha?
'''


# Aqui verificamos se uma entrada do dicionário de símbolos não terminais é válida ou não. 
# Para começar, se só tiver uma entrada não é necessário verificar.
def check_rule(rule_name, rules_list):
    # thing = ['Exp', "'$'"]
    for thing in rules_list:
        for exp in thing:
            is_terminal(exp)


def check_NT_Exists():
    #for pair in common.nterminal_dic:
    for rules in common.nterminal_dic.values():
        for rule in rules:
            for element in rule:
                # First we check if it is terminal
                is_terminal =  common.is_terminal(element) 
                # Then, we check if it non-terminal.
                if not is_terminal:
                    if element not in common.nterminal_dic.keys():
                        print(f"Simbol {element} has no rules associated.")
                        return False
    return True

# Função principal que verifica se a liguagem descrita nos dois dicionários é LL(1)
# Recebe dois dicionários, no primeiro aparece o nome do símbolo terminal associado à expressão regex que o descreve.
# No segundo estão associados nomes de regras com as respetivas especificações.
# Por exemplo, "Exp -> Termo '+' num" é decrito como (Exp, [ [Termo, '+', num] ]).
def main_check_LL1(terminal_dic_rec, nterminal_dic_rec):
    common.terminal_dic = terminal_dic_rec
    common.nterminal_dic = nterminal_dic_rec

    for expressao, rules_list in nterminal_dic_rec.items():
        #    check_rule(rule_name, rules_list)
        # follow('Exp', True )
        # expressao = 'Exp2'
        lista = look_ahead_main(expressao, [])
        print(f"[CheckLL1] Resultado de LA de {expressao} : {lista} ")
        if lista is None:
            print("Not LL(1), goodbye...")
            exit(1)
    #:w
    is_LL1 = check_NT_Exists()
    if not is_LL1:
        exit(1)

