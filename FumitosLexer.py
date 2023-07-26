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
        print(jSettings)
        if 'asm' not in outputPath:
            outputPath+ '.asm'
        outFile = open(outputPath, 'w')
        outFile.write(jSettings['initMain'])
        #improve the lexing/reading 
        for line in File.readlines():
            #some unhinged code ... why did i write this? why does it "work"?
            #i was something else durring hs
            for x in range(len(line)):
                if line[x] in self.operationsDict:
                    self.operationsDict[line[x]](outFile)
            # [self.operationsDict[char](outFile)  for char in self.operationsDict if line[x] == char]

        print('finished writing')
        outFile.write(jSettings['endMain'])



