import random
import copy


def random_edge(G):
    v1 = random.choice(list(G.keys()))
    v2 = random.choice(list(G[v1]))
    return v1, v2


def karger_min_cut(G):
    while len(G) > 2:
        v1, v2 = random_edge(G)  # choose edge
        G[v1].extend(G[v2])  # copy edges from V2 to V1
        for k in G[v2]:  # replacing V2 edges for V1 edges
            G[k].remove(v2)
            G[k].append(v1)
        while v1 in G[v1]:  # deleting self loops
            G[v1].remove(v1)
        del G[v2]  # deleting v2 vertex
    return len(G[list(G.keys())[0]])  # number of edges between the remaining 2 vertex


G = {}
# f = open('test.txt', 'r')
f = open('kargerMinCut.txt', 'r')
for line in f:
    tempInt = list(map(int, line.split()))
    my_dict = {tempInt[0]: tempInt for k in tempInt}
    del my_dict[tempInt[0]][0]
    G.update(my_dict)
f.close()

i = 0
count = 100000000
while i < 200:
    data = copy.deepcopy(G)
    min_cut = karger_min_cut(data)
    if min_cut < count:
        count = min_cut
    i += 1

print(count)  # min cut
