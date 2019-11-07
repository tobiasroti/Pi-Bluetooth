from bluepy import btle

class BTInterface(btle.DefaultDelegate):
    def __init__(self, deviceAddress):
            self.deviceAddress = deviceAddress
            btle.DefaultDelegate.__init__(self)

            # Address type must be "random" or it won't connect.
            self.peripheral = btle.Peripheral(deviceAddress, btle.ADDR_TYPE_RANDOM)
            self.peripheral.setDelegate(self)

            self.seq = 0
'''
            # Attribute UUIDs are identical to Ollie.
            self.antidos = self.getSpheroCharacteristic('2bbd')
            self.wakecpu = self.getSpheroCharacteristic('2bbf')
            self.txpower = self.getSpheroCharacteristic('2bb2')
            self.roll = self.getSpheroCharacteristic('2ba1')
            self.notify = self.getSpheroCharacteristic('2ba6')
'''
            # This startup sequence is also identical to the one for Ollie.
            # It even uses the same unlock code.
            print('Sending antidos')
            self.antidos.write('011i3', withResponse=True)
            print('Sending txpower')
            self.txpower.write('\x0007', withResponse=True)
            print('Sending wakecpu')
            self.wakecpu.write('\x01', withResponse=True)

test = BTInterface("DD:DB:26:00:0C:86")
