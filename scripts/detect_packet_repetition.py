from collections import Counter
import sys

filename = sys.argv[1]

with open(filename) as f:
    pkts = [line.strip() for line in f]


counts = Counter(pkts)
for pkt, cnt in counts.items():
    if cnt > 1:
        print(f"{pkt[:8]}... repeated {cnt} times")
    else:
        print("No repetition detected")
