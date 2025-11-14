from graph import Graph
#H
aplicaciones = Graph()

#A
aplicaciones.insert_vertex('Ubuntu', 'PC')
aplicaciones.insert_vertex('Mint', 'PC')
aplicaciones.insert_vertex('Fedora', 'PC')
aplicaciones.insert_vertex('Manjaro', 'PC')
aplicaciones.insert_vertex('Parrot', 'PC')
aplicaciones.insert_vertex('Debian', 'Notebook')
aplicaciones.insert_vertex('Red Hat', 'Notebook')
aplicaciones.insert_vertex('Arch', 'Notebook')
aplicaciones.insert_vertex('Impresora', 'Impresora')
aplicaciones.insert_vertex('Guarani', 'Servidor')
aplicaciones.insert_vertex('MongoDB', 'Servidor')
aplicaciones.insert_vertex('Switch1', 'Switch')
aplicaciones.insert_vertex('Switch2', 'Switch')
aplicaciones.insert_vertex('Router1', 'Router')
aplicaciones.insert_vertex('Router2', 'Router')
aplicaciones.insert_vertex('Router3', 'Router')

aplicaciones.insert_edge('Ubuntu', 'Switch1', 18)
aplicaciones.insert_edge('Mint', 'Switch1', 80)
aplicaciones.insert_edge('Impresora', 'Switch1', 22)
aplicaciones.insert_edge('Debian', 'Switch1', 17)
aplicaciones.insert_edge('Router1', 'Switch1', 29)
aplicaciones.insert_edge('Router2', 'Router1', 37)
aplicaciones.insert_edge('Router3', 'Router1', 43)
aplicaciones.insert_edge('Router2', 'Router3', 50)
aplicaciones.insert_edge('Router2', 'Red Hat', 25)
aplicaciones.insert_edge('Router2', 'Guarani', 9)
aplicaciones.insert_edge('Router3', 'Switch2', 61)
aplicaciones.insert_edge('Manjaro', 'Switch2', 40)
aplicaciones.insert_edge('Parrot', 'Switch2', 12)
aplicaciones.insert_edge('Fedora', 'Switch2', 3)
aplicaciones.insert_edge('Arch', 'Switch2', 56)
aplicaciones.insert_edge('MongoDB', 'Switch2', 5)

#B
#b. realizar un barrido en profundidad y amplitud partiendo desde la tres notebook:
#Red Hat, Debian, Arch;
print('barrido en profundidad desde Red Hat:')
aplicaciones.deep_sweep('Red Hat')

print()
print('barrido en amplitud desde Red Hat:')
aplicaciones.amplitude_sweep('Red Hat')
print()

print('barrido en profundidad desde Debian:')
aplicaciones.deep_sweep('Debian')

print()
print('barrido en amplitud desde Debian:')
aplicaciones.amplitude_sweep('Debian')
print()

print('barrido en profundidad desde Arch:')
aplicaciones.deep_sweep('Arch')

print()
print('barrido en amplitud desde Arch:')
aplicaciones.amplitude_sweep('Arch')
print()

#c
camino, peso = aplicaciones.shortest_path('Manjaro', 'Impresora')
print(f'camino más corto para imprimir desde Manjaro: {camino}, peso total: {peso}')

camino, peso = aplicaciones.shortest_path('Red Hat', 'Impresora')
print(f'camino más corto para imprimir desde Red Hat: {camino}, peso total: {peso}')

camino, peso = aplicaciones.shortest_path('Fedora', 'Impresora')
print(f'camino más corto para imprimir desde Fedora: {camino}, peso total: {peso}')

#D
minimo = aplicaciones.kruskal('Manjaro')
resultado = aplicaciones.print_kruskal(minimo)
print(resultado)
print()

minimo = aplicaciones.kruskal('Red Hat')
resultado = aplicaciones.print_kruskal(minimo)
print(resultado)
print()

minimo = aplicaciones.kruskal('Fedora')
resultado = aplicaciones.print_kruskal(minimo)
print(resultado)
print()

#E
destino = 'Guarani'
origenes =[]

for vertex in aplicaciones:
    if 'PC' in vertex.other_values:
        origenes.append(vertex.value)

print(origenes)

def comparar(grafo = Graph(), lista_origenes = list, destino = str):
    menor = 0
    while len(lista_origenes)>0:
        origen_actual = lista_origenes.pop()
        camino, peso = grafo.shortest_path(origen_actual, destino)
        if peso > menor:
            menor = peso
            origen_final = origen_actual
            camino_final = camino
    
    return origen_final, camino_final, menor

origen, camino, peso = comparar(aplicaciones, origenes, destino)

print(f'El camino más corto hacia {destino} es desde {origen}, haciendo el recorrido: {camino}')
print(f'peso: {peso}')

#F
destino = 'MongoDB'
origenes = []

for vertex in aplicaciones:
    for edge in vertex.edges:
        if 'Switch1' in edge.value and 'PC' in vertex.other_values:
            origenes.append(vertex.value)

print()

origen, camino, peso = comparar(aplicaciones, origenes, destino)

print(f'El camino más corto hacia {destino} en switch1 es desde {origen}, haciendo el recorrido: {camino}')
print(f'peso: {peso}')
print()

#G
aplicaciones.delete_edge('Impresora', 'Switch1', 'value')
aplicaciones.insert_vertex('Impresora', 'Router2')

print('barrido en profundidad desde Red Hat:')
aplicaciones.deep_sweep('Red Hat')

print()
print('barrido en amplitud desde Red Hat:')
aplicaciones.amplitude_sweep('Red Hat')
print()

print('barrido en profundidad desde Debian:')
aplicaciones.deep_sweep('Debian')

print()
print('barrido en amplitud desde Debian:')
aplicaciones.amplitude_sweep('Debian')
print()

print('barrido en profundidad desde Arch:')
aplicaciones.deep_sweep('Arch')

print()
print('barrido en amplitud desde Arch:')
aplicaciones.amplitude_sweep('Arch')
print()