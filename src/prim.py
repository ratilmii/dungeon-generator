import numpy as np

def minimum_spanning_tree(points, triangulation):
    """
    Luodaan minimum spanning tree käyttäen Primin algoritmia.
    Syötteenä saadaan lista (x, y) tupleja "points", joka pitää sisällään huoneiden keskipisteiden koordinaatit,
    sekä setti (i, j) tupleja "triangulation", jossa i ja j ovat points-listan indeksejä ja vastaavat hyväksyttyjen kolmioiden sivujen päätepisteitä.
    Funktio palauttaa setin (i, j) tupleja "result_edges" kuten triangulaatio, mutta sisältää vain minimimäärän sivuja.
    """

    cheapest_cost = {point: np.inf for point in points}
    cheapest_edge = {point: None for point in points}

    explored = set()
    unexplored = set(points)

    starting_point = points[0]
    cheapest_cost[starting_point] = 0

    # Sanakirja pisteiden välisille yhteyksille
    connections = {i: [] for i in range(len(points))}
    for i, j in triangulation:
        connections[i].append(j)
        connections[j].append(i)

    while unexplored:
        cheapest_point = min(unexplored, key=cheapest_cost.get)
        current_point = cheapest_point

        unexplored.remove(current_point)
        explored.add(current_point)

        current_point_idx = points.index(current_point)

        for neighbor_idx in connections[current_point_idx]:
            neighbor = points[neighbor_idx]
            w = weight(current_point, neighbor)

            if neighbor in unexplored and w < cheapest_cost[neighbor]:
                cheapest_cost[neighbor] = w
                cheapest_edge[neighbor] = (current_point_idx, neighbor_idx)
    
    result_edges = set()

    for point in points:
        if cheapest_edge[point] != None:
            result_edges.add(cheapest_edge[point])

    return result_edges

def weight(p1, p2):
    """"
    Laskee pisteiden p1 ja p2 välisen euklidisen etäisyyden numpyn avulla.
    Tämä etäisyys on minimum spanning treen kahden pisteen välinen paino, joka pyritään minimoimaan.
    """
    p1 = np.array(p1)
    p2 = np.array(p2)

    distance = np.linalg.norm(p2 - p1)

    return distance