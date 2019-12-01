INFINITY = 99999999999

while True:
    n, m, q = map(int, raw_input().split())
    if n == m == q == 0:
        break

    edge = []
    distan = [[INFINITY for _ in xrange(n)] for _ in xrange(n)]
    for _ in xrange(m):
        u, v, w = map(int, raw_input().split())
        dist[u][v] = min(w, dist[u[v]])

    for i in xrange(n):
        dist[i][i] = 0