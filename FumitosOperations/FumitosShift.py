import typing
def RightShiftIt(File:typing.TextIO,pointer : int or str ="RDX"):
    File.write(
f"""    inc {pointer}
"""
    )
def LeftShiftIt(File:typing.TextIO,pointer : int or str="RDX"):
    File.write(
f"""    dec {pointer}
"""
    )
    pass