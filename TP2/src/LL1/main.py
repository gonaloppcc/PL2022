from sys import argv

import parsing.LL1_sin as file_reader
import checkLL1.checkLL1 as checkLL1
from generator.generator import make

if __name__ == '__main__':
    input = "/home/banderas/Desktop/add_state_lexer/PL2022/TP2/files/test/temp.txt"
    if len(argv) >= 2:
        input = argv[1]
        print("Path to input file: ", input)

    output = "output"
    if len(argv) >= 3:
        output = argv[2]
        print("Path to output file: ", output)

    # Dictionaries that store the two types of data.
    #try:
    if True:
        file_reader.read_file(input)
        p = file_reader.read_file(input)
        print("-------------")
        #checkLL1.main_check_LL1(terminals, nterminals)
        checkLL1.main_check_LL1(p['tokens'], p['non_terminals'] )
        #print("Literals simbols: ", literals)

        #make(p, output)
    #except:
    #    print("Error")
    #    pass
