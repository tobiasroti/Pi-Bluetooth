from bluepy import btle

print ("Connecting...")
dev = btle.Peripheral("DD:DB:26:00:0C:86")

print ("Services...")
for svc in dev.services:
    print (str(svc))
