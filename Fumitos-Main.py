import os 
import sys
operationsChars = str("+-<>[]")
operationsList = {
    
    '+' : [" finsh addition!"],
    '-' : [" finish subtraction!"],
    '<' :[" finish pointer shift left!"],
    '>' : [" finish pointer shift right!"],
    '[' : [" finish loop_starter!"],
    ']' : [" finish loop_ender!"]
}



try:
    os.remove("test.txt")
except OSError:
    pass


try:
    global inFile
    if sys.argv == "--help":
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
    
.code 
    main proc
        
""")


PointerOffset:int = 0
for line in inFile.readlines():
    for operationsChars in line :
        print(operationsList[operationsChars])
        pass
else:#when EOF write this 
    outFile.write("""
    mov rdx, 1 ; rdx is first arguement within the windows x64 calling convention
    call ExitProcess
    main endp
end
    """)


