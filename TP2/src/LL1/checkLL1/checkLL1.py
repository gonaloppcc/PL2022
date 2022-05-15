from .look_ahead import look_ahead_main
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


# Check if all non terminal elements have a description.
def check_NT_Exists():
    # for pair in common.nterminal_dic:
    for rules in common.nterminal_dic.values():
        for rule in rules:
            for element in rule:
                # First we check if it is terminal
                is_terminal = common.is_terminal(element)
                # Then, we check if it non-terminal.
                if not is_terminal:
                    # If it's not terminal, it should be described in non-terminal dictionary.
                    if element not in common.nterminal_dic.keys():
                        print(f"[Error] Simbol {element} has no rules associated.")
                        return False
    return True


# Check if all states described in tokens exist.
def check_states(states_with_types: dict):
    state_names = states_with_types.keys()  # [x[0] for x in states_with_types]
    n_terminal_elements = common.terminal_dic.keys()
    state_n_terminals = [x[1] for x in n_terminal_elements]
    for verify_state in state_n_terminals:
        if verify_state not in state_names and verify_state != "INITIAL":
            print(f"[Error] State {verify_state} not described.")
            return False
    return True


# Função principal que verifica se a liguagem descrita nos dois dicionários é LL(1)
# Recebe dois dicionários, no primeiro aparece o nome do símbolo terminal associado à expressão regex que o descreve.
# No segundo estão associados nomes de regras com as respetivas especificações.
# Por exemplo, "Exp -> Termo '+' num" é decrito como (Exp, [ [Termo, '+', num] ]).
# noinspection PyPep8Naming
def main_check_LL1(terminal_dic_rec, nterminal_dic_rec, states, literals):
    common.terminal_dic = terminal_dic_rec
    common.nterminal_dic = nterminal_dic_rec
    common.literals = literals

    for expr, rules_list in nterminal_dic_rec.items():
        la = look_ahead_main(expr, [])  # Lookahead of expr
        print(f"[CheckLL1] Resultado de LA de {expr} : {la} ")
        if la is None:
            print("Not LL(1), goodbye...")
            exit(1)

    nt_valid = check_NT_Exists()
    states_valid = check_states(states)
    if not (nt_valid and states_valid):
        exit(1)
