import os
from sys import argv

import parsing.LL1_sin as file_reader
import checkLL1.checkLL1 as checkLL1

if __name__ == '__main__':
    #input = "../../files/test/input_recursivo_infinito2.txt"
    input = "../../files/test/input.txt"
    if len(argv) == 2:
        input = argv[1]
        print("Path to file: ", input)
    # Dictionarys that store the two types of data.
    # file_reader.read_file(input)
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
    except:
        pass