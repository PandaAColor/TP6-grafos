from graph import Graph

grafo_sw = Graph()

#A-D
grafo_sw.insert_vertex('Luke Skywalker', ['IV', 'V', 'VI', 'VIII', 'IX'])
grafo_sw.insert_vertex('Darth Vader', ['I', 'II', 'III', 'IV', 'V', 'VI'])
grafo_sw.insert_vertex('Yoda', ['I', 'II', 'III', 'V', 'VI', 'VIII'])
grafo_sw.insert_vertex('Boba Fett', ['II', 'V', 'VI'])
grafo_sw.insert_vertex('C-3PO', ['I','II','III', 'IV', 'V', 'VI', 'VII', 'VIII','IX'])
grafo_sw.insert_vertex('Leia', ['III', 'IV', 'V', 'VI', 'VII', 'VIII','IX'])
grafo_sw.insert_vertex('Rey', ['VII', 'VIII','IX'])
grafo_sw.insert_vertex('Kylo Ren', ['VII', 'VIII','IX'])
grafo_sw.insert_vertex('Chewbacca', ['III', 'IV', 'V', 'VI', 'VII', 'VIII','IX'])
grafo_sw.insert_vertex('Han Solo', ['IV', 'V', 'VI', 'VII','IX'])
grafo_sw.insert_vertex('R2-D2', ['I','II','III', 'IV', 'V', 'VI', 'VII', 'VIII','IX'])
grafo_sw.insert_vertex('BB-8', ['VII', 'VIII','IX'])

grafo_sw.insert_edge('Luke Skywalker', 'Leia', 5)
grafo_sw.insert_edge('Luke Skywalker', 'Han Solo', 4)
grafo_sw.insert_edge('Luke Skywalker', 'R2-D2', 4)
grafo_sw.insert_edge('Luke Skywalker', 'C-3PO', 4)
grafo_sw.insert_edge('Luke Skywalker', 'Yoda', 3)
grafo_sw.insert_edge('Luke Skywalker', 'Darth Vader', 3)
grafo_sw.insert_edge('Luke Skywalker', 'Rey', 2)
grafo_sw.insert_edge('Darth Vader', 'Leia', 2)
grafo_sw.insert_edge('Darth Vader', 'Yoda', 2)
grafo_sw.insert_edge('Darth Vader', 'Boba Fett', 2)
grafo_sw.insert_edge('Darth Vader', 'C-3PO', 2)
grafo_sw.insert_edge('Darth Vader', 'R2-D2', 2)
grafo_sw.insert_edge('Yoda', 'Leia', 2)
grafo_sw.insert_edge('Yoda', 'R2-D2', 2)
grafo_sw.insert_edge('Yoda', 'C-3PO', 2)
grafo_sw.insert_edge('Boba Fett', 'Han Solo', 2)
grafo_sw.insert_edge('Boba Fett', 'Chewbacca', 2)
grafo_sw.insert_edge('C-3PO', 'R2-D2', 9)
grafo_sw.insert_edge('C-3PO', 'Leia', 7)
grafo_sw.insert_edge('C-3PO', 'Han Solo', 4)
grafo_sw.insert_edge('C-3PO', 'Chewbacca', 4)
grafo_sw.insert_edge('C-3PO', 'Rey', 3)
grafo_sw.insert_edge('C-3PO', 'BB-8', 2)
grafo_sw.insert_edge('Leia', 'Chewbacca', 4)
grafo_sw.insert_edge('Leia', 'Han Solo', 4)
grafo_sw.insert_edge('Leia', 'R2-D2', 6)
grafo_sw.insert_edge('Leia', 'Rey', 3)
grafo_sw.insert_edge('Rey', 'Kylo Ren', 3)
grafo_sw.insert_edge('Rey', 'R2-D2', 2)
grafo_sw.insert_edge('Rey', 'BB-8', 3)
grafo_sw.insert_edge('Rey', 'Chewbacca', 3)
grafo_sw.insert_edge('Rey', 'Han Solo', 1)
grafo_sw.insert_edge('Kylo Ren', 'Leia', 3)
grafo_sw.insert_edge('Kylo Ren', 'Han Solo', 2)
grafo_sw.insert_edge('Kylo Ren', 'Luke Skywalker', 2)
grafo_sw.insert_edge('Chewbacca', 'Han Solo', 6)
grafo_sw.insert_edge('Chewbacca', 'R2-D2', 4)
grafo_sw.insert_edge('Han Solo', 'R2-D2', 4)
grafo_sw.insert_edge('R2-D2', 'BB-8', 2)

#B
max = grafo_sw.kruskal_max('C-3PO')
for edge in max.split(';'):
    print (edge)

print()
max = grafo_sw.kruskal_max('Yoda')
for edge in max.split(';'):
    print (edge)

print()
max = grafo_sw.kruskal_max('Leia')
for edge in max.split(';'):
    print (edge)

#C
def maximo_peso (grafo = Graph()):
    mayor = 0
    lista = []
    for vertex in grafo:
        for edge in vertex.edges:
            if edge.weight > mayor:
                lista = []
                mayor = edge.weight
            
            if mayor == edge.weight:
                lista.append(f'{vertex.value} - {edge.value}')
    return lista, mayor

lista_mayor, contador = maximo_peso(grafo_sw)

print(f'{lista_mayor}, episodios que comparten: {contador}')

#E
def apariciones(grafo = Graph()):
    lista = []
    for vertex in grafo:
        if len(vertex.other_values)== 9:
            lista.append(vertex.value)
    return lista

listado = apariciones(grafo_sw)
print(f'personajes que han aparecido en los 9 capítulos: {listado}')