def xo(s):
    if s:
        osarray = filter(lambda x: x.lower() =='o', s)
        xsarray = filter(lambda x: x.lower() =='x',s)

        if osarray and len(osarray) != len(xsarray):
            return False

    return True
