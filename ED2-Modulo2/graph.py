#!/usr/bin/env python

class Vertice(object):

    def __init__(self, n):

        #Se define el nombre del vertice y la lista de vecinos
        self.nombre = n
        self.vecinos = list()
    
    def agregarVecino(self, v):
        if v not in self.vecinos:
            self.vecinos.append(v)
            self.vecinos.sort()

class Grafo(object):

    #Se crea un diccionario de vertices.
    vertices = {}

    def agregarVertice(self, vertice):

        #Se pregunta si vertice es una instancia de Vertice y si el nombre no esta en la lista de vertices.
        #Si se cumple se agrega el vertice al diccionario de vertices.

        if isinstance(vertice, Vertice) and vertice.nombre not in self.vertices:
            self.vertices[vertice.nombre] = vertice
            return True
        else:
            return False

    def agregarBorde(self, u, v):

        #Si u y v estan en vertices. se agregan como vecinos.
        if u in self.vertices and v in self.vertices:
            self.vertices[u].agregarVecino(v)
            self.vertices[v].agregarVecino(u)
            return True
        else:
            return False

    def printGrafo(self):

        #Se muestra el grafo.
        for key in sorted(list(self.vertices.keys())):
            print(key + str(self.vertices[key].vecinos))

if __name__ == '__main__':

    g = Grafo()

    cinco = Vertice('5')
    tres = Vertice('3')
    cuatro = Vertice('4')
    uno = Vertice('1')
    dos = Vertice('2')

    for i in range(ord('1'), ord('6')):
        g.agregarVertice(Vertice(chr(i)))
        bordes = ['53','54','31','35','41','42','45','12','13','14','21','24']
    
    for borde in bordes:
        g.agregarBorde(borde[:1],borde[1:])
        g.printGrafo()