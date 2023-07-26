from FumitosOperations.FumitosArithmetic import *
from FumitosOperations.FumitosControlFlow import *
from FumitosOperations.FumitosShift import *

import typing
import json
#read InitSettings...
operationsDict = {
    
    '+' : IncrementIt,
    '-' : DeInrecrementIt,
    '<' : LeftShiftIt,
    '>' : RightShiftIt,
    '[' : CreateNewLoopLabel,
    ']' : EndLoopLabel,
    '.' : Print_

}

class ParseIntoAssembly:
    def __init__(self) -> None:
        self.operationsDict = {
    
            '+' : IncrementIt,
            '-' : DeInrecrementIt,
            '<' : LeftShiftIt,
            '>' : RightShiftIt,
            '[' : CreateNewLoopLabel,
            ']' : EndLoopLabel,
            '.' : Print_

        }

    def ParserMain(self, File:typing.TextIO, outputPath)->typing.TextIO:
        #return output file...
        jSettings = json.load(open('InitSettings.json'))
        if 'asm' not in outputPath:
            outputPath+ '.asm'
        outFile = open(outputPath, 'w')
        outFile.write(jSettings['initMain'])

        for line in File.readlines():
            [self.operationsDict[char](outFile) for x in range(len(line)) for char in self.operationsDict if line[x: x+len(char)] == char]

        print('finished writing')
        outFile.write(jSettings['endMain'])



