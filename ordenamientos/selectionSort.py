'''creacion del ordenamiento selectionsort'''
def selectionsort(lista):
    tam=len(lista)-1
    for i in range (0,tam):
        posMax=i
        for j in range (i+1,tam):#se buscara al menor de los menores
            if lista[j]<lista[posMax]:
                posMax=j
        menor=lista[j]
        lista[j]=lista[i]
        lista[i]=menor
    return lista

#TESTER
lista=[2,3,7,1,5]
print(lista)
selectionsort(lista)
print(lista)
            
