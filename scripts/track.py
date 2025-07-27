"""
This script is to check for the channel the mouse is using to communicate
"""

from rflib import *
import time

d = RfCat()
d.setMdmModulation(MOD_2FSK)
d.setEnableMdmDCFilter(False)
d.setEnableMdmManchester(False)
d.setMdmSyncMode(0)
d.setMaxPower()

freqs = [2426, 2427, 2428, 2430, 2448]

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
