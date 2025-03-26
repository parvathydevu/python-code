#process
def getspan(s, r):
    count = 0
    spans = []
    start = 0
    while True:
        start = s.find(r, start)
        if start == -1:
            break
        end = start + len(r)
        spans.append((start, end))
        count += 1
        start += 1  # Move to the next character to find subsequent occurrences
    return count, spans

# Input
s = 'mississippi'
r = 'ss'

# Output
count, spans = getspan(s, r)
print(f"Number of occurrences of '{r}' in '{s}': {count}")
print(f"Spans of '{r}' in '{s}': {spans}")
print(f"({count},{spans}")