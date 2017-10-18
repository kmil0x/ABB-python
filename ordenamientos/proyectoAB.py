'''contruccion de la clase nodo hoja'''
class hoja(object):
    def __init__(self,peso):#el peso indicara si la pos sera iz o derecha
        self.peso=peso
        self.pDer=None
        self.pIzq=None
    def getPeso(self):
        return self.peso
    def getHoja(self):
        return self
class arbol(object):
    def __init__(self):
        self.raiz=None
    def getVacio(self):
        if self.raiz==None:
            return True
    def agregarHoja(self,nuevo):
        if self.getVacio()==True:
            self.raiz=nuevo
        else:
            seguir=True
            temp=self.raiz
            while(seguir):
                if temp.getPeso()>=nuevo.getPeso() and temp.pIzq==None:
                    temp.pIzq=nuevo
                    seguir=False
                elif temp.getPeso()>=nuevo.getPeso():
                    temp=temp.pIzq
                if temp.getPeso()<nuevo.getPeso() and temp.pDer==None:
                    temp.pDer=nuevo
                    seguir=False
                elif temp.getPeso()<nuevo.getPeso():
                    temp=temp.pDer
    def setRaiz(self,newRaiz):
        self.raiz=newRaiz

