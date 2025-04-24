def compute_hash(n, elements):
    # Create tuple from the list of elements
    t = tuple(elements)
    # Compute and return the hash value of the tuple
    return hash(t)

# Read input values
n = int(input())
elements = list(map(int, input().split()))

# Compute and print the hash value
print(compute_hash(n, elements))