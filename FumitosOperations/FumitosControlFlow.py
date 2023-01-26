import typing
LabelCount =0
LabelStack = []
#Python's Devs, in their infanite and unbound wisdom, have decideded that 
#to use a global integer, i must use the global keyword!
def CreateNewLoopLabel(File:typing.TextIO, pointer:int or str = "RDX"):
    global LabelCount
    LabelCount+= 1
    LabelStack.append(F"{LabelCount}")
    File.write(
F"""    
    start_lblnum{LabelCount}: ; starting ----
    cmp qword ptr[{pointer}]
    jz end_lbl{LabelCount}
    ; middlle -----
"""
    )
    pass
def EndLoopLabel(File:typing.TextIO, pointer:int or str = "RDX"):
    global LabelCount
    templabel = LabelStack.pop()
    File.write(
F"""    
    cmp qword ptr[{pointer}], 0
    jnz start_lblnum{LabelCount}
    end_lbl{templabel}:; ending -----
"""
    )
    pass