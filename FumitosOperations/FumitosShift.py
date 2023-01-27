import typing
def RightShiftIt(File:typing.TextIO,pointer : int or str ="RDX"):
    #make sure you increment via byte offsets 
    File.write(
f"""    add {pointer}, 8
"""
    )
def LeftShiftIt(File:typing.TextIO,pointer : int or str="RDX"):
    File.write(
f"""    sub {pointer}, 8
"""
    )
    pass
def Print_(File:typing.TextIO,pointer : int or str="RDX"):
    File.write(
    F"""
    sub	rsp, 30h
	mov rcx, hStdOut
    push {pointer}
	mov rdx, offset CellPointer
	mov r8, 1
	call WriteFile
    pop {pointer}
	add rsp, 30h
    """  )