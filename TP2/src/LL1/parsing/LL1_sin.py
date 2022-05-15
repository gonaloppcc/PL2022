import ply.yacc as yacc
import sys

from typing import Dict

from parsing.LL1_lex import tokens, literals


# noinspection PyMethodMayBeStatic,PyShadowingNames,PyPep8Naming
class LL1_parser(object):

    def __init__(self, file_name):
        self.file_name = file_name
        self.tokens = tokens
        self.parser = yacc.yacc(module=self, start='Grammar', debug=False, optimize=0)
        self.parser.success = True
        self.parser.literals = set()  # Set of all the literals found TODO: Change this to be in the ast?

    def p_Grammar(self, p):
        "Grammar : Imports States TokensBoiler NonTerminalList"
        p[0] = {
            'imports': p[1],
            'states': p[2],
            'tokens': p[3],
            'literals': self.parser.literals,
            'non_terminals': p[4]
        }
        print(p[1])

    # -------------------------------- Begin Imports productions
    def p_Imports(self, p):
        "Imports : empty"
        p[0] = []

    def p_Imports_list(self, p):
        '''Imports : Imports Import
                   | Imports Import NEW_LINE'''
        p[0] = p[1] + [p[2]]

    def p_Import(self, p):
        "Import : IMPORT path"
        p[0] = {
            'path': p[2]
        }

    # ---------------------------------- End Imports productions

    # -------------------------------- Begin State productions
    def p_States_empty(self, p):
        "States : empty"
        p[0] = {}

    def p_States(self, p):
        "States : STATES ':' NEW_LINE StatesList"
        p[0] = p[4]

    def p_StatesList_elems(self, p):
        '''StatesList : StatesList State
                      | StatesList State NEW_LINE'''
        (state, incl) = p[2]
        p[1][state] = incl
        p[0] = p[1]

    def p_StatesList_empty(self, p):
        "StatesList : empty"
        p[0] = {}

    def p_State(self, p):
        "State : name Type"
        p[0] = (p[1], p[2])

    def p_Type_incl(self, p):
        "Type : incl"
        p[0] = p[1]

    def p_Type_excl(self, p):
        "Type : excl"
        p[0] = p[1]

    # -------------------------------- End State productions

    # -------------------------------- Begin Tokens productions
    def p_Tokens_boilerplate_empty(self, p):
        "TokensBoiler : empty"
        p[0] = {}

    def p_Tokens_boilerplate(self, p):
        "TokensBoiler : TOKENS ':' NEW_LINE Tokens"
        p[0] = p[4]

    def p_Tokens_list(self, p):
        '''Tokens : Tokens Token
                  | Tokens Token NEW_LINE'''
        nome = p[2]["name"]
        p[1][nome] = p[2]
        p[0] = p[1]

    def p_Tokens(self, p):
        "Tokens : empty"
        p[0] = {}

    def p_Token_State(self, p):
        "Token : tokenState expRegex Func NEW_LINE"
        p[0] = {
            "name": p[1],
            "regex": p[2],
            "func": p[3]

        }

    def p_Token_NoState(self, p):
        "Token : token expRegex Func NEW_LINE"
        p[0] = {
            "name": p[1],
            "regex": p[2],
            "func": p[3]
        }

    def p_Func_pop(self, p):
        "Func : pop"
        p[0] = p[1]

    def p_Func_push(self, p):
        "Func : push"
        p[0] = p[1]

    def p_Func_empty(self, p):
        "Func : empty"
        p[0] = None

    # -------------------------------- End Tokens productions

    # -------------------------------- Begin NonTerminal productions

    def p_NonTerminalList(self, p):  # Change this name to be not confused with *p_Tokens_list*
        "NonTerminalList : NonTerminalList NTerminal"
        p[1][p[2][0]] = p[2][1]
        # Creating an entry in the dictionary, p[1] is the dictionary,
        # p[2][0] the non-terminal simbol name and p[2][1] the definition the non-terminal

        p[0] = p[1]

    def p_NonTerminal(self, p):
        "NonTerminalList : empty"
        p[0] = {}  # TODO: Change this to be more efficient

    def p_NTerminal(self, p):
        "NTerminal : '-' NT ':' NEW_LINE Productions"
        p[0] = (p[2], p[5])

    def p_Productions(self, p):
        '''Productions : Production
                       | Production NEW_LINE'''
        p[0] = [p[1]]

    def p_Productions_list(self, p):
        '''Productions : Productions Production
                       | Productions Production NEW_LINE'''
        p[0] = p[1] + [p[2]]

    def p_Production_list(self, p):
        "Production : Production Simb"
        p[0] = p[1] + [p[2]]

    def p_Production_simb(self, p):
        "Production : Simb"
        p[0] = [p[1]]

    def p_Simb_empty(self, p):
        "Simb : EMPTY"
        p[0] = p[1]

    def p_Simb_literal(self, p):
        "Simb : literal"
        p[0] = p[1]
        p.parser.literals.add(p[1])  # TODO: p.parser OR self.parser ?????

    def p_Simb_NT(self, p):
        "Simb : NT"
        p[0] = p[1]

    def p_Simb_token(self, p):
        "Simb : token"
        p[0] = p[1]

    # -------------------------------- End NonTerminal productions

    # ------------------- Empty rule
    def p_empty(self, p):
        'empty :'

    # ---------------------- Handle Error function
    def p_error(self, p):
        if not p:
            print('Unexpected end of input!')
        elif p.type == 'NEW_LINE':  # Havoc solution of the NEW_LINE tokens that are interrupted with the comments.
            self.parser.errok()
            return
        else:
            print('Syntax Error:', f'{repr(p.value)}', f'in line {p.lineno}.')
        self.parser.success = False

    # ----------------------- Analyzing the input
    def ast_to_json(self, file_name: str, data):
        import json
        with open(file_name, 'w') as f:
            f.write(json.dumps(data))

    def join_ast(self, main: Dict, imported: Dict):
        # dict.update() # TODO: Change to static method

        print(imported)
        main['imports'] = main['imports'] + imported['imports']

        main['tokens'].update(imported['tokens'])

        main['literals'] = main['literals'].union(imported['literals'])

        main['non_terminals'].update(imported['non_terminals'])

    def recon(self, text: str) -> dict:
        """
        Using the defined lang, this function recons a given text, returning the ast (Abstract Syntax Tree).
        """

        # ----------------------- Analyzing the input
        ast = self.parser.parse(text)
        if self.parser.success:
            for imp in ast['imports']:
                with open(imp['path'], 'r') as f:
                    p = LL1_parser(imp['path'])
                    import_ast = p.recon(f.read())

                self.join_ast(ast, import_ast)

            print(f'Input text of {self.file_name} is correct...')
            # Prints to visualize the structures (debug)
            print('\tImports:', end=' ')
            print(*(ast['imports']), sep=', ')

            print('\tTokens:', end=' ')
            print(*(ast['tokens'].items()), sep=', ')

            print('\tLiterals:', end=' ')
            print(*(ast['literals']), sep=', ')

            print('\tNon-terminals:', end=' ')
            for n_term, prod in ast['non_terminals'].items():
                print(f'{n_term} -> ', prod, end=' ')

            print('\n\n')
        else:
            print(f'Input text of {self.file_name} is incorrect!!!')

        return ast


if __name__ == '__main__':
    p = LL1_parser('input.lly')
    p.recon(sys.stdin.read())


def read_file(input_file_name: str):
    file = open(input_file_name, 'r')
    content = file.read()

    p = LL1_parser(input_file_name)

    return p.recon(content)
