import sys
import FumitosLexer
lexer = FumitosLexer.ParseIntoAssembly()

try:
    if sys.argv[1] == "--help":
        print("compiler [filepath][optional = result]")
    inFile = open(sys.argv[1], 'r')
except FileNotFoundError :
    raise Exception("No Such file found!")
except IndexError:
    raise Exception("No File path given!")
if len(sys.argv) ==3:
    lexer.ParserMain(inFile, sys.argv[2])
elif len(sys.argv) ==2:
    lexer.ParserMain(inFile, 'a')
    #basically a.out ...
