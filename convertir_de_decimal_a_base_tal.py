def convertirABase(n,b):
    if n<0:
        return b
    else:
        return (n%b)+(convertirABase(n//10,b))
def convertirABaseTal(n,b):
    if n<b:
        return n
    else:
        return (n%b)+(10*convertirABaseTal(n//b,b))
print (convertirABaseTal(37,3))
