import os
from sys import argv

import file_reader.file_reader as file_reader
import checkLL1.checkLL1 as checkLL1

if __name__ == '__main__':
    input = "input.txt"
    if len(argv) == 2:
        input = argv[1]
        print("Path to file: ", input)
    # Dictionarys that store the two types of data.
    (terminals, nterminals) = file_reader.file_reader(input)
    print("Terminais:")
    for key, value in terminals.items():
        print(f"Key: {key} | Value: {value}")

    print("Não Terminais:")
    for key, value in nterminals.items():
        for rule in value.getRule():
            print(f"Key: {key} | One rule: {rule}")
    
    # Check if the file describes correctly an LL(1) language.
    checkLL1.main_check_LL1(terminals, nterminals)