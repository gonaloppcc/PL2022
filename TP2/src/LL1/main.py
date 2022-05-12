from sys import argv

import parsing.LL1_sin as file_reader
import checkLL1.checkLL1 as checkLL1
from generator.generator import make

if __name__ == '__main__':
    input = "input.txt"
    if len(argv) >= 2:
        input = argv[1]
        print("Path to input file: ", input)

    output = "output"
    if len(argv) >= 3:
        output = argv[2]
        print("Path to output file: ", output)

    # Dictionaries that store the two types of data.
    try:
        (terminals, nterminals, literals) = file_reader.read_file(input)
        print("Terminais:")
        for key, value in terminals.items():
            print(f"Key: {key} | Value: {value}")

        print("Não Terminais:")
        for key, value in nterminals.items():
            #print(key)
            #print(value)
            print("---------")
            for rule in value:
                print(f"Key: {key} | One rule: {rule}")

        # Check if the file describes correctly an LL(1) language.
        checkLL1.main_check_LL1(terminals, nterminals)
        print("Literals simbols: ", literals)

        make(terminals, nterminals, literals, output)
    except:
        pass
