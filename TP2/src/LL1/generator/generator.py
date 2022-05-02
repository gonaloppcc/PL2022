import generator.gen_lex as lex

def make(terminals, nterminals, file_path):
    with open(file_path, mode='w') as file:
        lex.make_lex(terminals, file)