from bluepy import btle

class BTInterface(btle.DefaultDelegate):
    def __init__(self, deviceAddress):
            self.deviceAddress = deviceAddress
            btle.DefaultDelegate.__init__(self)

            # Address type must be "random" or it won't connect.
            self.peripheral = btle.Peripheral(deviceAddress, btle.ADDR_TYPE_RANDOM)
            self.peripheral.setDelegate(self)

            #self.peripheral.writeCharacteristic(1, "test", withResponse=False)
            print(self.peripheral.getDescriptors())


test = BTInterface("DD:DB:26:00:0C:86")
