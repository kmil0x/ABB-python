'''creacion del ordenamiento bubblesort'''
def bubblesort(lista):
    tam=len(lista)-1
    for i in range (0,tam):#este for me ayuda a pasar entre los casilleros para compararlos
        for j in range (0,tam-i):#este for me realizara las comparaciones respectivas
            if lista[j]>lista[j+1]:
                temp=lista[j]#guardo el casillero que resulto mayor
                lista[j]=lista[j+1]
                lista[j+1]=temp#cambia de posicion las casillas
    return lista

#TESTER
lista=[2,3,7,1,5]
print(lista)
bubblesort(lista)
print(lista)
            
