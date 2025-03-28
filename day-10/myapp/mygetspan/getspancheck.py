import __main__
import string
from itertools import permutations

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

def reverseWords(s):
    return ' '.join(word[::-1] for word in s.split())

def removePunctuation(s):
    return s.translate(str.maketrans('', '', string.punctuation))

def countWords(s):
    return len(s.split())

def characterMap(s):
    return {char: s.count(char) for char in set(s)}

def makeTitle(s):
    return s.title()

def normalizeSpaces(s):
    return ' '.join(s.split())

def getPermutations(s):
    return [''.join(p) for p in permutations(s)]

if __name__ == "__main__":
    s = str(input("enter a full string: "))
    r = str(input("enter a substring: "))

# Output
    count, spans = getspan(s, r)
    print(f"({count},{spans})")

    print(f"Reversed words: {reverseWords(s)}")
    print(f"Without punctuation: {removePunctuation(s)}")
    print(f"Word count: {countWords(s)}")
    print(f"Character map: {characterMap(s)}")
    print(f"Title case: {makeTitle(s)}")
    print(f"Normalized spaces: {normalizeSpaces(s)}")
    print(f"Permutations: {getPermutations(s)}")