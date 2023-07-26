import os 
import sys
import FumitosLexer

try:
    os.remove("test.txt")
except OSError:
    pass


try:
    global inFile
    if sys.argv[1] == "--help":
        print("compiler [filepath][optional = result]")
    inFile = open(sys.argv[1], 'r')
except FileNotFoundError :
    print("No Such file found!")
    exit(-1)
except IndexError:
    print("No File path given!")
    exit(-1)
if len(sys.argv) ==3:
    try:
        global outFile
    except FileNotFoundError :
        print("No Such file found!")
        exit(-1)
    except IndexError:
        print("No File path given!")
        exit(-1)

lexer = FumitosLexer.ParseIntoAssembly()
lexer.ParserMain(inFile, sys.argv[2])
