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
# Simple function that return the intersection of two lists.
def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3

# Analises one rule and returns the simbol associated with the look ahead of this rule.
def analise_rule(expression, rule, la_visited : [str]):
    if rule[0] == expression:
        if common.debug:
            print("Left Recursivity")
        raise Not_LL1()
    if common.is_empty(rule[0]):
        if common.debug:
            print("Empty found")
        return follow.follow(expression, [])
    if common.is_terminal(rule[0]):
        if common.debug:
            print(f"Simbolo terminal {rule[0]} ")
        return [rule[0]]
    else:
        recursive_call = look_ahead_main(rule[0], [expression] + la_visited)
        if common.debug:
            print(f"Resultado recursivo de LA: {recursive_call} ")
        if recursive_call: 
            return recursive_call
        else: raise Not_LL1()


# Receives the expression we want to do the look ahead, and the look's ahead already done.
# The second argument is necessary to avoid infinite loops. 
def look_ahead_main(expression : str, la_visited : [str]):
    # if expression already analised, than it's not LL(1).
    if expression in la_visited:
        raise Not_LL1()
    # List of simbols that belong to the look ahead of the current expression.
    tsimbols_seen = []
    try:
        if common.debug:
             print(f"\n##### LA |{expression}| - START ####### \n")
        
    # Check if this expression has rules associated.
        if expression not in common.nterminal_dic:
            print(f"[LA of {expression}] Symbol {expression} has no description, and is necessary.")
            raise Not_LL1()
        
        # List of rules associated with the current expression
        list_rules = common.nterminal_dic[expression]
        for rule in list_rules:
            tsimbols_rule = analise_rule(expression, rule, la_visited)
            if not tsimbols_rule:
                raise Not_LL1()
            if len(intersection(tsimbols_rule , tsimbols_seen)) > 0:
                if common.debug:
                    print("There is intersection of simbols.")
                    print(tsimbols_rule)
                    print(tsimbols_seen)
                raise Not_LL1()
            else:
                if common.debug:
                    print(f"Add to visited simbols list: {tsimbols_rule}")
                tsimbols_seen = tsimbols_seen + tsimbols_rule
        
        if common.debug:
             print(f"\n---------- LA |{expression}| - END -------- \n")
        return tsimbols_seen
    except Not_LL1:
        print("Not LL1")