
#RCX is going to be used as the pointer offset
# 
import sys
import typing
PointerOffset:int = 0

def IncrementIt(File:typing.TextIO  ,pointer:int or str = "RDX" ):
    File.write(
F"""    inc qword ptr[{pointer}+ {PointerOffset}]
"""
    )
    pass
def DeInrecrementIt(File:typing.TextIO, pointer:int or str = "RDX"):
    File.write(
F"""    dec qword ptr[{pointer}+ {PointerOffset}]
"""
    )

    pass