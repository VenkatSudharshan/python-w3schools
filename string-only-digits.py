def onlyDigits(s):
    for ch in s:
        if(ch<'0' or ch>'9'):
            return False
    return True

print(onlyDigits("123"))