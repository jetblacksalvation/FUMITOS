
#RCX is going to be used as the pointer offset
# 
import sys
import typing
PointerOffset:int = 0

def IncrementIt(File:typing.TextIO,incrementBy:int  ,pointer:int or str = "RDX" ):
    File.write(
F"""    
    add qword ptr[{pointer}], {incrementBy}; called by IncrementIt
"""
    )
    pass
def DeInrecrementIt(File:typing.TextIO,incrementBy:int, pointer:int or str = "RDX"):
    File.write(
F"""    
    sub qword ptr[{pointer}], {incrementBy};called by DeIncrementIt
"""
    )

    pass