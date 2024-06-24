def q1(lista,string='A'):
    soma=0
    mult=1
    if string == 'A':
        i=0
        for numero in lista:
            soma += numero
            i+=1
        return soma/i
    if string == 'G':
        i=0
        for numero in lista:
            mult *= numero
            i+=1
        return mult**(1/i)
    if string == 'H':
        i=0
        for numero in lista:
            soma += 1/numero
            i+=1
        return i/soma
    else:
        return -1

# print(q1([25, 5]))
# print(q1([25, 5], 'A'))
# print(q1([3, 6, 9, 27], 'G'))
# print(q1([2, 2, 4, 4, 4, 4], 'H'))
# print(q1([1, 2, 3, 4, 5], 'B'))

def q2(numeradores,denominadores):
    lista = []
    for i in range(len(numeradores)):
        try:
            lista.append(numeradores[i]/denominadores[i])
        except TypeError:
            return -1
        except ZeroDivisionError:
            lista.append('inf')
            pass
        except IndexError:
            return lista
        
    return lista

# print(q2([3, 5, 4, 1], [2, 5, 2, 10]))
# print(q2([10.5, 4, 2.5, 3, '9.1'], [5, 10, '8', 4.3, 7.8]))
# print(q2([3, 4, 5], [1, 2, 'a']))
# print(q2([2.3, 4.1], [6.8, 1.9, 3.5, 2.7]))
# print(q2([1, 2, 5, 6, 3, 2], [2, 5, 8]))
# print(q2([0, 2, 4, 6, 8], [8, 0, 4, 2, 0]))

def q3(produtos):
    nome = input("Digite o nome do produto:")
    while b==True:
        try:
            if nome in produtos:
                print("Os valores serao alterados.")
                print(f"Valores cadastrados: preco={produtos[nome][0]}, peso={produtos[nome][1]}, preco/grama={produtos[nome][0]/produtos[nome][1]}")
                preco = input("Digite o preco desse produto: ")
                preco = float(preco)
                peso = input("Digite o peso desse produto:")
                if not(preco > 0 and preco < 100):
                    raise Intervalo
                if preco<0 or peso<0:
                    raise Negativo
                if peso==0:
                    raise Zero
                produtos[nome] = [preco, peso]
                b = False
            else:
                raise KeyError
        except KeyError:
            print("Inserindo o novo produto.")
            preco = input("Digite o preco desse produto: ")
            preco = float(preco)
            peso = input("Digite o peso desse produto:")
            if not(preco > 0 and preco < 100):
                raise Intervalo
            if preco<0 or peso<0:
                raise Negativo
            if peso==0:
                raise Zero
        except Intervalo:
            print("Valor invalido, digite um valor maior que 0 e menor que 100")
        except Negativo:
            print("Valor invalido, digite um numero não negativo")
        except Zero:
            print("O peso nao pode ser igual a zero.")
        

