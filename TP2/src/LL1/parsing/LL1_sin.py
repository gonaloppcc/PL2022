import ply.yacc as yacc
import sys

from typing import Dict

from LL1_lex import tokens, literals


# noinspection PyMethodMayBeStatic,PyShadowingNames
class LL1_parser(object):

    def __init__(self):
        self.tokens = tokens
        self.parser = yacc.yacc(module=self, write_tables=1, start='Grammar', debug=False, optimize=0)
        self.parser.success = True
        self.parser.literals = set()  # Set of all the literals found TODO: Change this to be in the ast?

    def p_Grammar(self, p):
        "Grammar : Imports TokensBoiler NonTerminalList"
        p[0] = {
            'imports': p[1],
            'tokens': p[2],
            'literals': self.parser.literals,
            'non_terminals': p[3]
        }

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

        # TODO: Add semantic action to import action

    def p_Tokens_boilerplate_empty(self, p):
        "TokensBoiler : empty"
        p[0] = {}

    def p_Tokens_boilerplate(self, p):
        "TokensBoiler : TOKENS ':' NEW_LINE Tokens"
        p[0] = p[4]

    def p_Tokens_list(self, p):
        '''Tokens : Tokens token
                  | Tokens token NEW_LINE'''
        p[1][p[2][0]] = p[2][1]
        p[0] = p[1]

    def p_Tokens(self, p):
        "Tokens : empty"
        p[0] = {}

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

    # ------------------- Empty rule
    def p_empty(self, p):
        'empty :'

    # ---------------------- Handle Error function
    def p_error(self, p):
        if not p:
            print('Unexpected end of input!')
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
        # main.update(imported)

        main['imports'] = main['imports'] + imported['imports']

        main['tokens'].update(imported['tokens'])

        main['literals'] = main['literals'].union(imported['literals'])

        main['non_terminals'].update(imported['non_terminals'])

    def recon(self, text: str) -> dict:
        """
        Using the defined lang, this function recons a given text, returning the ast (Abstract Syntax Tree).
        """

        ast = self.parser.parse(text)
        # TODO: Add arbitary new lines to the sintaxe
        if self.parser.success:
            for imp in ast['imports']:
                with open(imp['path'], 'r') as f:
                    p = LL1_parser()
                    import_ast = p.recon(f.read())

                self.join_ast(ast, import_ast)

            # Print pretty stuff
            # from tabulate import tabulate
            # print('\t\t\t\t\tAST:\n', tabulate(ast, headers="keys"))
            print('\tImports:', end=' ')
            for imp in ast['imports']:
                print(f'path: {imp}', end=' ')

            print('\n\tTokens:', end=' ')
            for tok in ast['tokens']:
                print(f'{tok}:', ast['tokens'][tok], end=' ')

            print('\n\tLiterals:', end=' ')
            for lit in ast['literals']:
                print(f'{lit}', end=' ')

            print('\n\tNon-terminals:', end=' ')
            for n_term, prod in ast['non_terminals'].items():
                print(f'{n_term} -> ', prod, end=' ')

            print('\n\n')
        else:
            print('!!! Invalid input text !!!')

        return ast


if __name__ == '__main__':
    p = LL1_parser()
    p.recon(sys.stdin.read())
