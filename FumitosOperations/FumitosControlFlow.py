import typing

global Labelcount; Labelcount :int= 0

def CreateNewLoopLabel(File:typing.TextIO, pointer:int or str = "RDX", labelcount = Labelcount):
    labelcount += 1
    
    File.write(
"""    label_num{}:
""".format(Labelcount)
    )
    pass
def EndLoopLabel(File:typing.TextIO, pointer:int or str = "RDX",labelcount = Labelcount):
    labelcount +=1
    File.write(
"""    
    cmp qword ptr[{}], 0
    jz label_num{}
    jmp  label_num{}
    label_num{}:
""".format(pointer,labelcount, labelcount-1,labelcount)
    )
    pass