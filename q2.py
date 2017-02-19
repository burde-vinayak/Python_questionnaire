def convert(a):
    try:
        a = int(a)
        return a
    except:
        pass
    try:
        a = float(a)
        return a
    except:
        pass
    return a

print type(convert('1'))
print type(convert('1.0'))
print type(convert('abc'))