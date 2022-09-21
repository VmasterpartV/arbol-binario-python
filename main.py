from arbol import Arbol

arbol_numeros = Arbol(5)
arbol_numeros.agregar(2)
arbol_numeros.agregar(9)
arbol_numeros.agregar(10)
arbol_numeros.agregar(20)
arbol_numeros.agregar(10)
arbol_numeros.agregar(25)
arbol_numeros.preorden()
arbol_numeros.inorden()
arbol_numeros.postorden()

busqueda = int(input("Ingresa un número para buscar en el árbol: "))
n = arbol_numeros.buscar(busqueda)
if n is None:
    print(f"{busqueda} no existe")
else:
    print(f"{busqueda} sí existe")

remover = int(input("Ingresa un número para remover del árbol: "))
n = arbol_numeros.remove(remover)
arbol_numeros.preorden()
arbol_numeros.inorden()
arbol_numeros.postorden()