from Graph import Graph


def test_dfs():
    arr = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    g = Graph(arr)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    g.add_edge(2, 3)
    g.add_edge(3, 5)
    g.add_edge(5, 6)
    g.add_edge(5, 7)
    g.add_edge(6, 8)

    g.dfs(0)


def test_dfs_recursive():
    arr = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    g = Graph(arr)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    g.add_edge(2, 3)
    g.add_edge(3, 5)
    g.add_edge(5, 6)
    g.add_edge(5, 7)
    g.add_edge(6, 8)

    g.dfs_recursive_first(0)


def test_bfs():
    arr = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    g = Graph(arr)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    g.add_edge(2, 3)
    g.add_edge(3, 5)
    g.add_edge(5, 6)
    g.add_edge(5, 7)
    g.add_edge(6, 8)

    g.bfs(0)


if __name__ == '__main__':
    #
    #        0
    #      /
    #    1 -- 3   7
    #    |  /  \ /
    #    | /    5
    #    2 -- 4  \
    #             6 -- 8

    print("DFS: ", end='')
    test_dfs()
    print("DFS Recursive: ", end='')
    test_dfs_recursive()
    print("BFS: ", end='')
    test_bfs()
