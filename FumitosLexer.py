from FumitosOperations.FumitosArithmetic import *
from FumitosOperations.FumitosControlFlow import *
from FumitosOperations.FumitosShift import *

import typing
import json

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
        self.lastChar = ''
        self.charCounter =1
        self.incrementList = ['+','-','<','>']

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
            for char in line:
                if self.lastChar != char and self.lastChar in self.incrementList:
                    self.operationsDict[self.lastChar](outFile,self.charCounter)
                    print('called', self.lastChar, self.charCounter, 'times')
                    self.charCounter =1
                if self.lastChar!=char:
                    self.lastChar = char

                elif char in self.incrementList and char == self.lastChar:
                    self.charCounter +=1
                    pass
                if char not in self.incrementList and char in self.operationsDict:
                    self.operationsDict[char](outFile)
                    print('called function for',char)
                        

            # [self.operationsDict[char](outFile)  for char in self.operationsDict if line[x] == char]

        print('finished writing')
        outFile.write(jSettings['endMain'])
        outFile.close()


