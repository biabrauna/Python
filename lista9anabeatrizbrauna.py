def q1(arq,mesa):
    c = open(arq,'r')
    for linha in c:
        mesaNumReal = linha.split(',')
        if int(mesaNumReal[0][5:]) == mesa:
            return linha
    c.close()
    return ''

# print(q1('2024_1_rest1.txt',1))
# print(q1('2024_1_rest1.txt',10))
# print(q1('2024_1_rest1.txt',20))
# print(q1('2024_1_rest2.txt',1))

def q2(arq,mesa):
    c = open(arq,'r')
    b = False
    soma = 0
    total_pessoas = 0
    for linha in c:
        mesaNumReal = linha.split(',') 
        if int(mesaNumReal[0][5:]) == mesa:
            pessoas = int(mesaNumReal[1])
            precos_float = [float(preco) for preco in mesaNumReal[3::2]]
            soma += sum(precos_float)
            b = True
            total_pessoas += pessoas 
    c.close()
    if b == True:
        media = soma/total_pessoas
        return soma, media
    else:
        return 0.0
    
# print(q2('2024_1_rest1.txt',1))
# print(q2('2024_1_rest1.txt',10))
# print(q2('2024_1_rest1.txt',20))
# print(q2('2024_1_rest2.txt',20))
# print(q2('2024_1_rest2.txt',1))
# print(q2('2024_1_rest2.txt',10))
# print(q2('2024_1_rest3.txt',4))


def q3(arq,arqCriado,mesas):
    c = open(arq,'r')
    cCriado = open(arqCriado,'w')
    for linha in c:
        mesaNumReal = linha.split(',')
        if int(mesaNumReal[0][5:]) in mesas:
            cCriado.write(linha)
    c.close()
    cCriado.close()
    return 0

# print(q3( '2024_1_rest1.txt','2024_1_rest1Novo1.txt',[1,2,7,10,20] ))
# print(q3( '2024_1_rest1.txt','2024_1_rest1Novo2.txt', [20,10,7,2,1] ))
# print(q3( '2024_1_rest1.txt','2024_1_rest1Novo3.txt', [2,7,10] ))
# print(q3( '2024_1_rest2.txt','2024_1_rest2Novo1.txt',[1]))


def q4(arq):
    dicionario1={}
    dicionario2={}
    c = open(arq,'r')
    for linha in c:
        precos = linha.split(',')
        for i in range(2, len(precos) - 1, 2):
                chave = precos[i]
                valor = float(precos[i + 1])
                dicionario1[chave] = valor
                if chave in dicionario2:
                    dicionario2[chave] += 1
                else:
                    dicionario2[chave] = 1
    c.close()
    return dicionario1,dicionario2
        
# print(q4( '2024_1_rest1.txt' ))
# print(q4( '2024_1_rest2.txt' ))
# print(q4( '2024_1_rest3.txt' ))

           


