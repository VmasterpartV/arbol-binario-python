from nodo import Nodo

class Arbol:
    # Funciones privadas
    def __init__(self, dato):
        self.raiz = Nodo(dato)

    def __agregar_recursivo(self, nodo, dato):
        if dato < nodo.dato:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(dato)
            else:
                self.__agregar_recursivo(nodo.izquierda, dato)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(dato)
            else:
                self.__agregar_recursivo(nodo.derecha, dato)

    def __inorden_recursivo(self, nodo):
        if nodo is not None:
            self.__inorden_recursivo(nodo.izquierda)
            print(nodo.dato, end=", ")
            self.__inorden_recursivo(nodo.derecha)

    def __preorden_recursivo(self, nodo):
        if nodo is not None:
            print(nodo.dato, end=", ")
            self.__preorden_recursivo(nodo.izquierda)
            self.__preorden_recursivo(nodo.derecha)

    def __postorden_recursivo(self, nodo):
        if nodo is not None:
            self.__postorden_recursivo(nodo.izquierda)
            self.__postorden_recursivo(nodo.derecha)
            print(nodo.dato, end=", ")

    def __buscar(self, nodo, busqueda):
        if nodo is None:
            return None
        if nodo.dato == busqueda:
            return nodo
        if busqueda < nodo.dato:
            return self.__buscar(nodo.izquierda, busqueda)
        else:
            return self.__buscar(nodo.derecha, busqueda)

    def __remove(self,nodo,dato):
        if(nodo.dato == dato):        
            if(nodo.derecha!= None):
                nodo.derecha,dato = self.delmin(nodo.derecha)
                newnodo = Nodo(dato)
                newnodo.derecha = nodo.derecha
                newnodo.izquierda = nodo.izquierda
                return newnodo
            elif(nodo.izquierda!=None):
                nodo.izquierda,dato = self.delmax(nodo.izquierda)
                newnodo = Nodo(dato)
                newnodo.derecha = nodo.derecha
                newnodo.izquierda = nodo.derecha
                return newnodo
            else:
                return None
        elif(nodo.dato > dato):
            nodo.izquierda = self.__remove(nodo.izquierda,dato)
            return nodo
        else:
            nodo.derecha = self.__remove(nodo.derecha,dato)
            return nodo

    
    def delmin(self,nodo):
        if(nodo.izquierda == None):
            return nodo.derecha,nodo.dato
        else:
            nodo.izquierda,key = self.delmin(nodo.izquierda)
            return nodo,key
    def delmax(self,nodo):
        if(nodo.derecha == None):
            return nodo.izquierda,nodo.dato
        else:
            nodo.derecha,key= self.delmax(nodo.derecha)


    # Funciones públicas

    def agregar(self, dato):
        self.__agregar_recursivo(self.raiz, dato)

    def inorden(self):
        print("Imprimiendo árbol inorden: ")
        self.__inorden_recursivo(self.raiz)
        print("")

    def preorden(self):
        print("Imprimiendo árbol preorden: ")
        self.__preorden_recursivo(self.raiz)
        print("")

    def postorden(self):
        print("Imprimiendo árbol postorden: ")
        self.__postorden_recursivo(self.raiz)
        print("")

    def buscar(self, busqueda):
        return self.__buscar(self.raiz, busqueda)

    def remove(self, dato):
        self.raiz = self.__remove(self.raiz, dato)