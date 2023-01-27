import os 
import sys
from FumitosOperations.FumitosArithmetic import *
from FumitosOperations.FumitosControlFlow import *
from FumitosOperations.FumitosShift import *
operationTokens = ["+", "-", "<", ">", "[", "]", "."]
operationsDict = {
    
    '+' : IncrementIt,
    '-' : DeInrecrementIt,
    '<' : LeftShiftIt,
    '>' : RightShiftIt,
    '[' : CreateNewLoopLabel,
    ']' : EndLoopLabel,
    '.' : Print_

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
GetStdHandle proto
WriteFile proto	
ReadFile proto	
ExitProcess  proto	
.data
	
    hStdIn dq	?; stdin 
    hStdOut dq	?;stdout
    CellPointer qword 1000 dup(0)
.code 
    main proc
    	sub rsp, 28h        ; space for 4 arguments + 16byte aligned stack
	;-------getting handles ---
	;----stdin
	mov rcx, -11
	call GetStdHandle
	mov hStdOut, rax; DWORD hStdOut = GetStdHandle(-11);
	;-----stdout
	mov rcx, -10
	call GetStdHandle
	mov hStdIn, rax;DWORD hStdIn = GetStdHandle(-10);

	add rsp, 28h
	;-------end getting handles 
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


