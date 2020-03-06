def convertir_decimal(pNum,pBase, pExpo=0):
    if pNum < pBase :
        return pNum*pBase**pExpo
    else:
        return (pNum%10*pBase**pExpo + convertir_decimal(pNum//10,pBase, pExpo+1))
print(convertir_decimal(100101001,2))
