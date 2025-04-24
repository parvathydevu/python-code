def qbot(m, n, games, q, queries):
    result = []
    for query in queries:
        count = 0
        for game in games:
            if query in game:
                count += 1
        result.append((query, count))
    return result

size = input('Size of games (Example 2 3) -> ')
m, n = map(int, size.split())
q = int(input("Enter the count of queries: "))

games = []
for _ in range(m):
    games.append(list(map(int, input().split()))[:n])

queries = list(map(int, input("Enter the queries: ").split()))
print(qbot(m, n, games, q, queries))