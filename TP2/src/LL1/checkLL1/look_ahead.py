#from checkLL1.common import terminal_dic, nterminal_dic, is_terminal
import checkLL1.common as common
import checkLL1.follow as follow
''' 
Here we check the follow of a expression.
'''

class Error(Exception):
    """Base class for other exceptions"""
    pass

class Not_LL1(Error):
    """Raised when the input value is too small"""
    pass

def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3

def analise_rule(expression, rule):
    if rule[0] == expression:
        print("Recursividade à esquerda")
        raise Not_LL1()
    if common.is_empty(rule[0]):
        print("Empty")
        return follow.follow(expression, [])
    if common.is_terminal(rule[0]):
        print(f"Simbolo terminal {rule[0]} ")
        return [rule[0]]
    else:
        recursivo = look_ahead_main(rule[0])
        print(f"Resultado recursivo de LA: {recursivo} ")
        if recursivo: 
            return recursivo
        else: raise Not_LL1()



def look_ahead_main(expression):
    tsimbols_seen = []
    try:
        print(f"\n##### LA |{expression}| - START ####### \n")
        list_rules = common.nterminal_dic[expression]
        for rule in list_rules:
            tsimbols_rule = analise_rule(expression, rule)
            if not tsimbols_rule:
                raise Not_LL1()
            if len(intersection(tsimbols_rule , tsimbols_seen)) > 0:
                print("Existe interseção de símbolos")
                print(tsimbols_rule)
                print(tsimbols_seen)
                raise Not_LL1()
            else:
                print(f"Adicionou à lista de símbolos visitados: {tsimbols_rule}")
                tsimbols_seen = tsimbols_seen + tsimbols_rule
        
        print(f"\n---------- LA |{expression}| - END -------- \n")
        return tsimbols_seen
    except Not_LL1:
        print("Not LL1")