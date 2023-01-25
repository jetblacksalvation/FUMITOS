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
    inFile = open(sys.argv[1])
except FileNotFoundError :
    print("No Such file found!")
    exit(-1)
except IndexError:
    print("No File path given!")
    exit(-1)
outFile = open("test.txt", 'a')

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



for line in inFile.readlines():
    for operationsChars in line :
        print(operationsList[operationsChars])#invoke function here 
        pass
else:#when EOF write this 
    outFile.write("""
    mov rdx, 1 ; rdx is first arguement within the windows x64 calling convention
    call ExitProcess
    main endp
end
    """)


