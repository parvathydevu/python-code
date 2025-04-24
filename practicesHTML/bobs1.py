# input the size of the game
size = input('Size of of games (Example 2 3) -> ')
try:
    m, n, *x = list(map(int, size.split()))
except:
    print("Invalid input")

# ----------- Games ----------- #
games = []
print(f"Specify {m} games of length {n} -> values sepated by space (Example 1 3 3 -1)")
for _ in range(m):
    game = input("Game -> ")
    try:
        game = list(map(int, game.split()))[:n]
    except:
        game = [0 for _ in range(n)]
        print("Invalid input")
    games.append(game)


# ----------- Sequences ----------- #
nseq = int(input("N -> "))
seqs = []
print(f"Specify {nseq} sequences -> values sepated by space (Example 1 3 3 -1)")
for _ in range(nseq):
    s = input("Sequence -> ")
    try:
        s = list(map(int, s.split()))
    except:
        s = [0 for _ in range(nseq)]
        print("Invalid input")
    seqs.append(s)

# output
print("\nGames: ", games)
print("Sequences: \n", seqs)

result = []
for seq in seqs:
    count = 0
    for game in games:
        if seq == game[:len(seq)]:
            count += 1
    result.append((seq, count))

print("Result -> ")
print(result)