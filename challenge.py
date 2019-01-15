def decompress(str):
    if simplestring(str):
        content = getcontent(str)
        num = getnum(str)
        content *= num
        print(content)
    else:
        stringarray = simplify(str)
        for i in stringarray:
            decompress(i)


def simplestring(str):
    ob = '['
    count_ob = 0
    for i in str:
        if i == ob:
            count_ob += 1
            if count_ob > 1:
                return False
    return True


def getcontent(str):
    i = str.index('[') + 1
    j = str.index(']')
    return str[i:j]


def getnum(str):
    if str.index('[') > 0:
        i = str.index('[')
        return int(str[:i])
    else:
        return 0


def simplify(str):
    return


decompress('[abc]')
