from math import log2

def shannon_entropy(data: str) -> float:
    if not data:
        return 0
    freq = {char: data.count(char) for char in set(data)}
    return -sum((count / len(data)) * log2(count / len(data)) for count in freq.values())
