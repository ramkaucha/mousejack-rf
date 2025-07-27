from rflib import *
import time
import math
from collections import Counter
import select
import sys


def shannon_entropy(data):
    if not data:
        return 0

    counter = Counter(data)
    total = len(data)

    return -sum((count / total) * math.log2(count/total) for count in counter.values())


def enter_pressed():
    return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])


d = RfCat()
d.setMdmModulation(MOD_2FSK)
d.setEnableMdmDCFilter(False)
d.setFreq(243000000)
d.setEnableMdmManchester(False)
d.setMdmSyncMode(0)
d.setMaxPower()

print("Start interating with the mouse...")

try:
    while True:
        pkt, _ = d.RFrecv(timeout=1000)
        if pkt:
            with open("packets.txt", 'a') as f:
                f.write(pkt.hex() + "\n")
            print(f"{pkt[:4].hex()}... len={len(pkt)}")

        if enter_pressed():
            print("Enter pressed, stopping the capture")
            break
except KeyboardInterrupt:
    d.setModeIDLE()
    print("\nCompleted")
finally:
    d.setModeIDLE()
    print("\nCompleted")

with open("packets.txt") as f:
    for line in f:
        pkt = bytes.fromhex(line.strip())
        print(shannon_entropy(pkt))
