"""
This script is to check for the channel the mouse is using to communicate
"""

from rflib import *
import time
from collections import defaultdict

no_activity = []

d = RfCat()
d.setMdmModulation(MOD_2FSK)
d.setEnableMdmDCFilter(False)
d.setEnableMdmManchester(False)
d.setMdmSyncMode(0)
d.setMaxPower()

print("\n Starting frequency sweep, keep the mouse idle")

packet_counts = defaultdict(int)
threshold = 4  # low to no activity

for freq in range(2402, 2481):
    hz = freq * 1000000
    d.setFreq(hz)
    print(f"Scanning {freq} MHz...")

    count = 0

    for _ in range(10):
        try:
            pkt, _ = d.RFrecv(timeout=200)
            if pkt:
                count += 1
        except:
            pass

    packet_counts[freq] = count
    print(f"Packets captured: {count}")

# d.setModeIDLE()
print("Scanning Completed.")

print("\n * Freq that had low / no activity")

freqs = []

for freq, count in packet_counts.items():
    if count < threshold:
        print(f"{freq} MHz has {count} packets")
        freqs.append(freq)


print("Starting to track changes in packets between idle & active")
res = {}
for freq in freqs:
    hz = freq * 1000000
    d.setFreq(hz)

    print("Starting IDLE phase...\n")
    input("Do not move the mouse. Press ENTER to begin...")
    idle = []
    start = time.time()
    while time.time() - start < 10:
        try:
            pkt, _ = d.RFrecv(timeout=1000)
            if pkt:
                idle.append(time.time())
        except ChipconUsbTimeoutException:
            print("Timeout - no packets received")

    print(f"\nCaptured {len(idle)} packets in idle phase...")

    input("Move the mouse now. Press ENTER to begin...")
    active = []
    start = time.time()
    while time.time() - start < 10:
        try:
            pkt, _ = d.RFrecv(timeout=1000)
            if pkt:
                active.append(time.time())
        except ChipconUsbTimeoutException:
            print("Timeout - no packets received")
    print(f"\nCaptured {len(active)} packets in active phase...")\

    res[freq] = {"idle": len(idle), "active": len(active)}


d.setModeIDLE()

print("\nSummary:")
for freq, counts in res.items():
    print(f"{freq} MHz - IDLE: {counts['idle']} | ACTIVE: {counts['active']}")
