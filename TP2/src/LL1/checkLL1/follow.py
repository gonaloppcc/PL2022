# from checkLL1.common import terminal_dic, nterminal_dic, is_terminal
import checkLL1.common as common
import checkLL1.look_ahead as look_ahead


class Error(Exception):
    """Base class for other exceptions"""
    pass


class Not_LL1(Error):
    """Raised when the input value is too small"""
    pass


# Não sei como é o follow de A em: C -> A b A d
def analise_rule(expression, rule_name, rule, follows_done):
    '''Structure.md'''
    res = []
    positions = indices = [index for index, element in enumerate(rule) if element == expression]
    if len(positions) > 0:
        for expression_position in positions:
            print(f"Expression |{expression}| found in rule |{rule}|  ")
            if expression_position + 1 == len(rule):
                if rule_name not in (follows_done, expression):
                    print(f"1Faz follow de |{rule_name}|")
                    recursivo = follow(rule_name, [expression] + follows_done)
                    if recursivo or len(recursivo) == 0:
                        res = res + recursivo
                    else:  # É none, logo não é LL1
                        raise Not_LL1()
            elif common.is_terminal(rule[expression_position + 1]):
                print(f"Encontrou terminal | {rule[expression_position + 1]}|")
                res.append(rule[expression_position + 1])
            else:
                print(f"2Faz LA de | {expression_position + 1}|")
                recursivo = look_ahead.look_ahead_main(rule[expression_position + 1], [])
                if recursivo:
                    res = res + recursivo
                else:
                    raise Not_LL1()
    return res


def analise_list_rules(expression, rule_name, rule_list, follows_done):
    simbols = []
    for rule in rule_list:
        res = analise_rule(expression, rule_name, rule, follows_done)
        if len(res) > 0:
            simbols = simbols + res
    return simbols


def follow(expression, follows_done):
    try:
        if expression in follows_done:
            print("Não devia estar aqui, esta expressão já teve follow")
            return []
        tsimbols_seen = []
        print(f"\n##### FOLLOW |{expression}| - START ####### \n")
        for rule_name, rules_objects in common.nterminal_dic.items():
            res = analise_list_rules(expression, rule_name, rules_objects.getRule(), follows_done)
            if len(res) > 0:
                tsimbols_seen = tsimbols_seen + res
        print(f"\n---------- Follow |{expression}| - END -------- ")
        print(f"---------- answer |{set(tsimbols_seen)}|  -------- \n")
        return list(set(tsimbols_seen))
    except Not_LL1:
        return None
