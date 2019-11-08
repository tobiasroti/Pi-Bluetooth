'''
import time

class ScanDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)

    def handleDiscovery(self, dev, isNewDev, isNewData):
        if isNewDev:
            print "Discovered device", dev.addr
        elif isNewData:
            print "Received new data from", dev.addr

scanner = Scanner().withDelegate(ScanDelegate())
devices = scanner.scan(10.0)

arudino = ''


for dev in devices:
    print "Device %s (%s), RSSI=%d dB" % (dev.addr, dev.addrType, dev.rssi)
    if dev.addr == 'dd:db:26:00:0c:86':
        print("FUCK")
        arudino = dev
    for (adtype, desc, value) in dev.getScanData():
        print "  %s = %s" % (desc, value)
while True:
    print("call")
    scanner.handleDiscovery(arudino, False, True)
    time.sleep(1)


'''

# import the necessary parts of the bluepy library
from bluepy.btle import Scanner, DefaultDelegate

# create a delegate class to receive the BLE broadcast packets
class ScanDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)

    # when this python script discovers a BLE broadcast packet, print a message with the device's MAC address
    def handleDiscovery(self, dev, isNewDev, isNewData):
        if dev.addr == 'dd:db:26:00:0c:86':
            if isNewDev:
                print "Discovered device", dev.addr
            elif isNewData:
                print "Received new data from", dev.addr

# create a scanner object that sends BLE broadcast packets to the ScanDelegate
scanner = Scanner().withDelegate(ScanDelegate())

# start the scanner and keep the process running
scanner.start()
while True:
    print "Still running..."
    scanner.process()
    print(scanner.ScanEntry.connectable)
