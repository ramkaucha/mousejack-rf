from rflib import *
import time

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
            print(f"{pkt[:4].hex()}... len={len(pkt)}")
except KeyboardInterrupt:
    d.setModeIDLE()
    print("\nCompleted")
