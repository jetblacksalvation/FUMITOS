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
    cmp qword ptr[{pointer}],0
    jz end_lblnum{LabelCount}
    ; scope start ----- {LabelCount}
"""
    )
    pass
def EndLoopLabel(File:typing.TextIO, pointer:int or str = "RDX"):
    global LabelCount
    templabel = 0
    try :
        templabel= LabelStack.pop()
    except IndexError:
        print("You have an extra ] or it's mis-matched")
        exit(-1)
    File.write(
f"""
    ;scope end ---- {templabel}
    cmp qword ptr[{pointer}], 0
    jnz start_lblnum{LabelCount}
    end_lblnum{templabel}:; ending -----
"""
    )
    pass