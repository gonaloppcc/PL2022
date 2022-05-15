# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "GrammarCOMMENT EMPTY IMPORT MULTICOMMENT NEW_LINE NT STATES TOKENS excl expRegex incl literal name path pop push token tokenStateGrammar : Imports States TokensBoiler NonTerminalListImports : emptyImports : Imports Import\n                   | Imports Import NEW_LINEImport : IMPORT pathStates : emptyStates : STATES ':' NEW_LINE StatesListStatesList : StatesList State\n                      | StatesList State NEW_LINEStatesList : emptyState : name TypeType : inclType : exclTokensBoiler : emptyTokensBoiler : TOKENS ':' NEW_LINE TokensTokens : Tokens Token\n                  | Tokens Token NEW_LINETokens : emptyToken : tokenState expRegex Func NEW_LINEToken : token expRegex Func NEW_LINEFunc : popFunc : pushFunc : emptyNonTerminalList : NonTerminalList NTerminalNonTerminalList : emptyNTerminal : '-' NT ':' NEW_LINE ProductionsProductions : Production\n                       | Production NEW_LINEProductions : Productions Production\n                       | Productions Production NEW_LINEProduction : Production SimbProduction : SimbSimb : EMPTYSimb : literalSimb : NTSimb : tokenempty :"

_lr_action_items = {'STATES': ([0, 2, 3, 5, 12, 14, ], [-37, 7, -2, -3, -4, -5, ]),
                    'IMPORT': ([0, 2, 3, 5, 12, 14, ], [-37, 8, -2, -3, -4, -5, ]), 'TOKENS': (
    [0, 2, 3, 4, 5, 6, 12, 14, 18, 22, 23, 27, 33, 34, 35, 36, ],
    [-37, -37, -2, 11, -3, -6, -4, -5, -37, -7, -10, -8, -9, -11, -12, -13, ]), '-': (
    [0, 2, 3, 4, 5, 6, 9, 10, 12, 14, 15, 16, 18, 19, 21, 22, 23, 25, 26, 27, 30, 33, 34, 35, 36, 38, 41, 42, 43, 44,
     45, 46, 47, 53, 54, 55, 56, 57, 58, ],
    [-37, -37, -2, -37, -3, -6, -37, -14, -4, -5, 20, -25, -37, -24, -37, -7, -10, -15, -18, -8, -16, -9, -11, -12, -13,
     -17, -35, -26, -27, -32, -33, -34, -36, -29, -28, -31, -19, -20, -30, ]), '$end': (
    [0, 1, 2, 3, 4, 5, 6, 9, 10, 12, 14, 15, 16, 18, 19, 21, 22, 23, 25, 26, 27, 30, 33, 34, 35, 36, 38, 41, 42, 43, 44,
     45, 46, 47, 53, 54, 55, 56, 57, 58, ],
    [-37, 0, -37, -2, -37, -3, -6, -37, -14, -4, -5, -1, -25, -37, -24, -37, -7, -10, -15, -18, -8, -16, -9, -11, -12,
     -13, -17, -35, -26, -27, -32, -33, -34, -36, -29, -28, -31, -19, -20, -30, ]), 'NEW_LINE': (
    [5, 13, 14, 17, 27, 29, 30, 34, 35, 36, 39, 40, 41, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 55, 56, 57, ],
    [12, 18, -5, 21, 33, 37, 38, -11, -12, -13, -37, -37, -35, 54, -32, -33, -34, -36, 56, -21, -22, -23, 57, 58, -31,
     -19, -20, ]), ':': ([7, 11, 24, ], [13, 17, 29, ]), 'path': ([8, ], [14, ]),
                    'name': ([18, 22, 23, 27, 33, 34, 35, 36, ], [-37, 28, -10, -8, -9, -11, -12, -13, ]), 'NT': (
    [20, 37, 41, 42, 43, 44, 45, 46, 47, 53, 54, 55, 58, ],
    [24, 41, -35, 41, 41, -32, -33, -34, -36, 41, -28, -31, -30, ]),
                    'tokenState': ([21, 25, 26, 30, 38, 56, 57, ], [-37, 31, -18, -16, -17, -19, -20, ]), 'token': (
    [21, 25, 26, 30, 37, 38, 41, 42, 43, 44, 45, 46, 47, 53, 54, 55, 56, 57, 58, ],
    [-37, 32, -18, -16, 47, -17, -35, 47, 47, -32, -33, -34, -36, 47, -28, -31, -19, -20, -30, ]),
                    'incl': ([28, ], [35, ]), 'excl': ([28, ], [36, ]), 'expRegex': ([31, 32, ], [39, 40, ]), 'EMPTY': (
    [37, 41, 42, 43, 44, 45, 46, 47, 53, 54, 55, 58, ], [45, -35, 45, 45, -32, -33, -34, -36, 45, -28, -31, -30, ]),
                    'literal': ([37, 41, 42, 43, 44, 45, 46, 47, 53, 54, 55, 58, ],
                                [46, -35, 46, 46, -32, -33, -34, -36, 46, -28, -31, -30, ]),
                    'pop': ([39, 40, ], [49, 49, ]), 'push': ([39, 40, ], [50, 50, ]), }

_lr_action = {}
for _k, _v in _lr_action_items.items():
    for _x, _y in zip(_v[0], _v[1]):
        if not _x in _lr_action:  _lr_action[_x] = {}
        _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'Grammar': ([0, ], [1, ]), 'Imports': ([0, ], [2, ]),
                  'empty': ([0, 2, 4, 9, 18, 21, 39, 40, ], [3, 6, 10, 16, 23, 26, 51, 51, ]), 'States': ([2, ], [4, ]),
                  'Import': ([2, ], [5, ]), 'TokensBoiler': ([4, ], [9, ]), 'NonTerminalList': ([9, ], [15, ]),
                  'NTerminal': ([15, ], [19, ]), 'StatesList': ([18, ], [22, ]), 'Tokens': ([21, ], [25, ]),
                  'State': ([22, ], [27, ]), 'Token': ([25, ], [30, ]), 'Type': ([28, ], [34, ]),
                  'Productions': ([37, ], [42, ]), 'Production': ([37, 42, ], [43, 53, ]),
                  'Simb': ([37, 42, 43, 53, ], [44, 44, 55, 55, ]), 'Func': ([39, 40, ], [48, 52, ]), }

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
    for _x, _y in zip(_v[0], _v[1]):
        if not _x in _lr_goto: _lr_goto[_x] = {}
        _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
    ("S' -> Grammar", "S'", 1, None, None, None),
    ('Grammar -> Imports States TokensBoiler NonTerminalList', 'Grammar', 4, 'p_Grammar', 'LL1_sin.py', 20),
    ('Imports -> empty', 'Imports', 1, 'p_Imports', 'LL1_sin.py', 32),
    ('Imports -> Imports Import', 'Imports', 2, 'p_Imports_list', 'LL1_sin.py', 36),
    ('Imports -> Imports Import NEW_LINE', 'Imports', 3, 'p_Imports_list', 'LL1_sin.py', 37),
    ('Import -> IMPORT path', 'Import', 2, 'p_Import', 'LL1_sin.py', 41),
    ('States -> empty', 'States', 1, 'p_States_empty', 'LL1_sin.py', 50),
    ('States -> STATES : NEW_LINE StatesList', 'States', 4, 'p_States', 'LL1_sin.py', 54),
    ('StatesList -> StatesList State', 'StatesList', 2, 'p_StatesList_elems', 'LL1_sin.py', 58),
    ('StatesList -> StatesList State NEW_LINE', 'StatesList', 3, 'p_StatesList_elems', 'LL1_sin.py', 59),
    ('StatesList -> empty', 'StatesList', 1, 'p_StatesList_empty', 'LL1_sin.py', 65),
    ('State -> name Type', 'State', 2, 'p_State', 'LL1_sin.py', 69),
    ('Type -> incl', 'Type', 1, 'p_Type_incl', 'LL1_sin.py', 73),
    ('Type -> excl', 'Type', 1, 'p_Type_excl', 'LL1_sin.py', 77),
    ('TokensBoiler -> empty', 'TokensBoiler', 1, 'p_Tokens_boilerplate_empty', 'LL1_sin.py', 84),
    ('TokensBoiler -> TOKENS : NEW_LINE Tokens', 'TokensBoiler', 4, 'p_Tokens_boilerplate', 'LL1_sin.py', 88),
    ('Tokens -> Tokens Token', 'Tokens', 2, 'p_Tokens_list', 'LL1_sin.py', 92),
    ('Tokens -> Tokens Token NEW_LINE', 'Tokens', 3, 'p_Tokens_list', 'LL1_sin.py', 93),
    ('Tokens -> empty', 'Tokens', 1, 'p_Tokens', 'LL1_sin.py', 99),
    ('Token -> tokenState expRegex Func NEW_LINE', 'Token', 4, 'p_Token_State', 'LL1_sin.py', 103),
    ('Token -> token expRegex Func NEW_LINE', 'Token', 4, 'p_Token_NoState', 'LL1_sin.py', 112),
    ('Func -> pop', 'Func', 1, 'p_Func_pop', 'LL1_sin.py', 120),
    ('Func -> push', 'Func', 1, 'p_Func_push', 'LL1_sin.py', 124),
    ('Func -> empty', 'Func', 1, 'p_Func_empty', 'LL1_sin.py', 128),
    ('NonTerminalList -> NonTerminalList NTerminal', 'NonTerminalList', 2, 'p_NonTerminalList', 'LL1_sin.py', 136),
    ('NonTerminalList -> empty', 'NonTerminalList', 1, 'p_NonTerminal', 'LL1_sin.py', 144),
    ('NTerminal -> - NT : NEW_LINE Productions', 'NTerminal', 5, 'p_NTerminal', 'LL1_sin.py', 148),
    ('Productions -> Production', 'Productions', 1, 'p_Productions', 'LL1_sin.py', 152),
    ('Productions -> Production NEW_LINE', 'Productions', 2, 'p_Productions', 'LL1_sin.py', 153),
    ('Productions -> Productions Production', 'Productions', 2, 'p_Productions_list', 'LL1_sin.py', 157),
    ('Productions -> Productions Production NEW_LINE', 'Productions', 3, 'p_Productions_list', 'LL1_sin.py', 158),
    ('Production -> Production Simb', 'Production', 2, 'p_Production_list', 'LL1_sin.py', 162),
    ('Production -> Simb', 'Production', 1, 'p_Production_simb', 'LL1_sin.py', 166),
    ('Simb -> EMPTY', 'Simb', 1, 'p_Simb_empty', 'LL1_sin.py', 170),
    ('Simb -> literal', 'Simb', 1, 'p_Simb_literal', 'LL1_sin.py', 174),
    ('Simb -> NT', 'Simb', 1, 'p_Simb_NT', 'LL1_sin.py', 179),
    ('Simb -> token', 'Simb', 1, 'p_Simb_token', 'LL1_sin.py', 183),
    ('empty -> <empty>', 'empty', 0, 'p_empty', 'LL1_sin.py', 190),
]
