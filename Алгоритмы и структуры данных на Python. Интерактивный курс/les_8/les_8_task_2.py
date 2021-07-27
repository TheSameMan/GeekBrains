'''2. Доработать алгоритм Дейкстры (рассматривался на уроке),
чтобы он дополнительно возвращал список вершин, которые
необходимо обойти.
'''


from random import randint
from collections import namedtuple

def rand_graph(N):
    adj_dict = {k: set() for k in range(N)}

    Edge = namedtuple('Edge', ['vi', 'vj', 'wij'])
    edges = [Edge(vi, vj, wij=randint(1, 3 * N)) for vi in range(N)
         for vj in range(vi, randint(vi, N)) if vi != vj]

    for edge in edges:
        adj_dict[edge.vi].add((edge.vj, edge.wij))
        adj_dict[edge.vj].add((edge.vi, edge.wij))

    return adj_dict

def dijkstra(graph, start):
    is_visited = [False] * len(graph)
    cost = dict.fromkeys({k for k in graph.keys()}, float('inf'))
    path_to = {k: [float('inf')] for k in graph.keys()}
    pass_path = []

    cost[start] = 0
    path_to[start] = [start]
    vi= start
    prev_v = vi
    while True:

        pass_path.append(vi)
        is_visited[vi] = True
        min_w = float('inf')
        for vj, wij in graph[vi]:

            if not is_visited[vj]:
                if wij + cost[prev_v] < cost[vj]:
                    cost[vj] = wij + cost[prev_v]

                    if path_to[vj][0] == float('inf'):
                        path_to[vj].pop(0) 
                    path_to[vj].extend(path_to[prev_v])
                    path_to[vj].append(vj)

                if wij < min_w:
                    min_w = wij
                    vi = vj

        if prev_v == vi:
            break

        prev_v = vi

    print('Вершины обхода гарфа:', *pass_path)

    print(f'Стоимость прохода до вершин:')
    for v, c in cost.items():
        print(f'Вершина {v}:', c)

    print(f'Кратчайшие пути до вершин:')
    for v, p in path_to.items():
        print(f'Вершина {v}:', *p)

try:
    print('Поиск вершин обхода по Алгоритму Дейкстры.')

    N = int(input('Введите число вершин: '))
    graph = rand_graph(N)
    print('Список смежности случайного графа:')
    print(*graph.items(), sep='\n')

    dijkstra(graph, 4)
except ValueError:
    print('Ошибка ввода.')