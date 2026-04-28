from grove.adc import ADC
import time
from datetime import datetime
from grove.grove_relay import GroveRelay

adc = ADC(address=0x08)          
CHANNEL = 0          
relay = GroveRelay(16) 

KUIVA = 823
MARKA = 313

def kosteus_prosentti():
    adc_arvo = adc.read(CHANNEL)
    kosteus = (KUIVA - adc_arvo) / (KUIVA - MARKA) * 100
    return max(0, min(100, kosteus))

def kastelu():
    kosteus = kosteus_prosentti()
    print(f"Kosteus: {kosteus:.1f} %")

    if kosteus < 60:
        print("Relay ON")
        relay.on()
        time.sleep(5)
        print("Relay OFF")
        relay.off()
        

kastelu()