import numpy as np

def circumcircle_contains(p1, p2, p3, p):
    """
    Palauttaa True mikäli piste p on kolmion (p1, p2, p3) ympäröivän ympyrän sisällä.
    """

    p1, p2, p3, p = [np.array(pt, dtype=float) for pt in (p1, p2, p3, p)]
    
    matrix = np.array([
        [p1[0], p1[1], p1[0]**2 + p1[1]**2, 1],
        [p2[0], p2[1], p2[0]**2 + p2[1]**2, 1],
        [p3[0], p3[1], p3[0]**2 + p3[1]**2, 1],
        [p[0],  p[1],  p[0]**2 + p[1]**2,   1]
    ])

    det = np.linalg.det(matrix)

    # Pisteiden muodostaman kolmion orientaatio
    orient = (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])
    # Jos pisteet samalla viivalla
    tolerance = 1e-9
    if abs(orient) < tolerance:
        return False
    elif orient > 0:
        return det > tolerance
    else:
        return det < -tolerance

def make_super_triangle(points):
    """
    Luodaan super triangle joka sisältää varmasti kaikki pisteet.
    """

    min_x, max_x = np.min(points[:, 0]), np.max(points[:, 0])
    min_y, max_y = np.min(points[:, 1]), np.max(points[:, 1])
    dx = max_x - min_x
    dy = max_y - min_y
    scaling = max(dx, dy)
    midx = (min_x + max_x) / 2
    midy = (min_y + max_y) / 2

    return [
        (midx - 20 * scaling, midy + scaling),
        (midx, midy - 20 * scaling),
        (midx + 20 * scaling, midy + scaling)
    ]

def triangulate(points):
    """"
    Triangulaatio Bowyer-Watson-menetelmällä.    
    points-parametri luolaston generoinnista saatu lista (x,y) tupleja.
    Palauttaa listan kolmioita muodossa [[i, j, k],...], jossa i, j, k ovat points-listan indeksejä.
    """
    
    if len(points) < 3:
        return set()
    
    points = np.array(points, dtype=float)
    n = len(points)

    super_triangle = make_super_triangle(points)

    super_vertices = [np.array(pt, dtype=float) for pt in super_triangle]
    points = np.vstack([points, super_vertices])
    super_indices = list(range(n, n + 3))

    triangulation = [super_indices]

    for i in range(n):
        badTriangles = []
        for triangle in triangulation:
            if circumcircle_contains(points[triangle[0]], points[triangle[1]], points[triangle[2]], points[i]):
                badTriangles.append(triangle)
        
        polygon = set()
        for triangle in badTriangles:
            for j in range(3):
                edge = tuple(sorted([triangle[j], triangle[(j + 1) % 3]]))
                if edge in polygon:
                    polygon.remove(edge)
                else:
                    polygon.add(edge)
        
        triangulation = [t for t in triangulation if t not in badTriangles]

        for edge in polygon:
            newTri = [i, edge[0], edge[1]]
            triangulation.append(newTri)

    triangulation = [t for t in triangulation if not any(v in super_indices for v in t)]    
    
    return triangulation

def get_edges(triangulation):
    """
    Palauttaa triangulaatiosta saatujen kolmioiden sivut settinä (i, j)-tupleja, jotka vastaavat points-listan indeksejä.
    """

    edges = set()
    for triangle in triangulation:
        for j in range(3):
            edge = tuple(sorted([triangle[j], triangle[(j + 1) % 3]]))
            edges.add(edge)

    return edges