from sys import argv

from parsing.LL1_sin import read_file
import checkLL1.checkLL1 as checkLL1
from generator.generator import make

if __name__ == '__main__':
    input_file_name = "input.txt"
    if len(argv) >= 2:
        input_file_name = argv[1]
        print("Input file path:", input_file_name)

    output = "output"
    if len(argv) >= 3:
        output = argv[2]
        print("Output file path:", output)

    # Dictionaries that store the two types of data.
    try:
        ast = read_file(input_file_name)

        terminals = ast['tokens']
        nterminals = ast['non_terminals']
        literals = ast['literals']
        states = ast['states']

        # Check if the file describes correctly an LL(1) language.
        is_valid = checkLL1.main_check_LL1(terminals, nterminals, states, literals)
        if not is_valid:
            exit(1)

        make(states, terminals, nterminals, literals, output)
    except FileNotFoundError:
        print('Invalid file path!')
