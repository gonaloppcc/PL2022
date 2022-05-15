import gen_lex as lex
import gen_top_down as td


def make(terminals, nterminals, literals, file_path):
    lex_file = f'{file_path}_lex'
    top_down = f'{file_path}_top_down'

    with open(lex_file + '.py', mode='w') as file_lex:
        lex.make_lex(terminals, literals, file_lex)
    with open(top_down + '.py', mode='w') as file_top_down:
        td.make_top_down(nterminals, terminals, literals, lex_file, file_top_down)
