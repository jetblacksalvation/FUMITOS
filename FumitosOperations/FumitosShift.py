import typing
def RightShiftIt(File:typing.TextIO,pointer : int or str ="RDX"):
    File.write(
"""    inc {}
""".format(pointer)
    )
def LeftShiftIt(File:typing.TextIO,pointer : int or str="RDX"):
    File.write(
"""    dec {}
""".format(pointer)
    )
    pass