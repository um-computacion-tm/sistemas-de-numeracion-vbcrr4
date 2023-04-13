def binario2decimal (binario):
    total=0
    for i in range (0,len(binario)):
        total+= int(binario[-i-1]) *2**i
    return total
def decimal2binario(decimal):
    resultado= ""
    resultadoinvertido= ""
    while decimal >= 2:
        resultadoinvertido += str(decimal%2)
        decimal = decimal//2
    resultadoinvertido += str(decimal)
    for i in range(0,len(resultadoinvertido)):
        resultado = resultado + resultadoinvertido[-i-1]
    while len(resultado) % 8 != 0:
        resultado = "0" + resultado
    return resultado

if __name__=="__main__":
    pass   