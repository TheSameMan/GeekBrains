'''3. Написать программу, которая обходит не взвешенный
ориентированный граф без петель, в котором все вершины связаны,
по алгоритму поиска в глубину (Depth-First Search).
Примечания:
a. граф должен храниться в виде списка смежности;
b. генерация графа выполняется в отдельной функции, которая
принимает на вход число вершин.
'''


from random import randint, sample
from collections import deque

def rand_graph(N):
    adj_dict = dict.fromkeys(range(N), [])

    for vi in adj_dict.keys():

        verts = tuple(v for v in range(N) if v != vi)
        adj_dict[vi] = {vj for vj in sample(verts, randint(1, N-1))}

    return adj_dict

def search(graph, item, start, mode='deep'):
    queue, passed = deque([start], maxlen=len(graph)), {start}

    if mode == 'breadth':
        queue_get = queue.pop
    elif mode == 'deep':
        queue_get = queue.popleft
    else:
        del queue
        del passed
        return 'Error mode.'

    print(f'Search item: {item}\nMode: {mode}')
    step = 0
    while queue:
        i_vertex = queue_get()
        print(f'step {step}: vertex {i_vertex}')
        if i_vertex == item:
            return 'Item found.\n'

        for j_vertex in graph.get(i_vertex):
            if j_vertex not in passed:
                passed.add(j_vertex)
                queue.appendleft(j_vertex)

        step += 1
    else:
        return 'Item not found.\n'


try:
    print('Depth-First Search.')

    N = int(input('Enter the number of vertices: '))
    item = int(input('Enter the search item: '))
    start = randint(0, N-1)
    graph = rand_graph(N)
    print('Graph adjacency list:')
    print(*graph.items(), sep='\n')
    print()

    print(f'Start vertex: {start}')
    print(search(graph, item, start))
except ValueError:
    print('Input Error.')
