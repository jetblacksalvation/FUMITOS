import os 
import sys
from FumitosOperations.FumitosArithmetic import *
from FumitosOperations.FumitosControlFlow import *
from FumitosOperations.FumitosShift import *
operationTokens = ["+", "-", "<", ">", "[", "]"]
operationsDict = {
    
    '+' : IncrementIt,
    '-' : DeInrecrementIt,
    '<' : LeftShiftIt,
    '>' : RightShiftIt,
    '[' : CreateNewLoopLabel,
    ']' : EndLoopLabel
}



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
        os.remove(sys.argv[2])
        outFile = open(sys.argv[2], 'a')
    except FileNotFoundError :
        print("No Such file found!")
        exit(-1)
    except IndexError:
        print("No File path given!")
        exit(-1)

#File Reading 
outFile.write("""
; Remember This Tagets x64! 
includelib kernel32.lib
includelib msvcrt.lib
ExitProcess  proto
.data
    CellPointer qword 1000 dup(0)
.code 
    main proc
    mov rdx, offset CellPointer
""")


for line in inFile.readlines():
    [operationsDict[char](outFile) for x in range(len(line)) for char in operationTokens if line[x: x+len(char)] == char]
    # for chars in line :
    #     if chars in operationTokens:
            
    #         operationsDict[chars](outFile)
    #     pass
else:#when EOF write this 
    outFile.write("""
    mov rdx, 1 ; rdx is first arguement within the windows x64 calling convention
    call ExitProcess
    main endp
end
    """)


