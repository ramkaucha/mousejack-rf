import sys
import math
from collections import Counter

def shannon_entropy(data):
    if not data:
        return 0

    counter = Counter(data)
    total = len(data)

    return -sum((count / total) * math.log2(count/total) for count in counter.values())


filename = sys.argv[1]

with open(filename, 'r') as f:
    for line in f:
        pkt = bytes.fromhex(line.strip())
        with open("packet_entropy", 'a') as w:
            w.write(str(shannon_entropy(pkt)) + '\n')
