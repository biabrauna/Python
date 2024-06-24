def q1(n):
    if n == 1 or n == 2:
        return 1
    elif n == 3:
        return 2
    else:
        return q1(n-1) + q1(n-2) + q1(n-3)

# print(q1(1))  
# print(q1(2)) 
# print(q1(3)) 
# print(q1(4))  
# print(q1(5)) 

def q2(n):
    if n == 0:
        return 0
    else:
        return n + q2(n-1)

# print(q2(0)) 
# print(q2(1))  
# print(q2(5))  

def q3(x, y):
    if x < y:
        return x
    elif x == y:
        return 0
    else:
        return q3(x - y, y)

# print(q3(2, 5))  
# print(q3(10, 3)) 
# print(q3(10, 4))  
# print(q3(10, 5)) 

def q4(lista):
    if not lista:
        return []
    else:
        primeiro = lista[0]
        resto_lista = q4([x for x in lista[1:] if x != primeiro])
        return [primeiro] + resto_lista

# print(q4([1, 2, 3]))      
# print(q4([1, 2, 1, 3, 1])) 
# print(q4([1, 2, 1, 2]))   
# print(q4([2, 2, 2, 2]))    
# print(q4([1, 2, 3, 2, 1])) 
