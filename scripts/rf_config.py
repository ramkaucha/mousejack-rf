from rflib import *
import time

d = RfCat()

d.setFreq(2479)

d.setMdmModulation(MOD_2FSK)

# d.setMdmDRate(2000000)

d.setEnableMdmDCFilter(False)

d.setEnableMdmManchester(False)

d.setMdmSyncMode(0)

d.setMaxPower()

print("\n * RF Configuration Complete")

try:
    while True:
        pkt, _ = d.RFrecv(timeout=1000)
        if pkt:
            print(f"* Packet: {pkt.hex()} (len={len(pkt)})")
except KeyboardInterrupt:
    print("\n* Done")
    d.setModeIDLE()
