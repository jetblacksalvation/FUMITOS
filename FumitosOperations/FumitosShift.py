import typing
def RightShiftIt(File:typing.TextIO,pointer : int or str ="RDX"):
    #make sure you increment via byte offsets 
    File.write(
f"""    add {pointer}, 8
"""
    )
def LeftShiftIt(File:typing.TextIO,pointer : int or str="RDX"):
    File.write(
f"""    add {pointer}, 8
"""
    )
    pass