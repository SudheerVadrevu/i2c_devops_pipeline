import time
from waveform.i2c_visualizer import I2CSignalVisualizer

class I2CDevice:
    def __init__(self, address):
        self.address = address

    def respond(self):
        return f"ACK from device {hex(self.address)}"

class Clock:
    def tick(self):
        return "Clock Tick"

if __name__ == '__main__':
    devices = [I2CDevice(addr) for addr in [0x10, 0x20, 0x30]]
    clock = Clock()

    print(clock.tick())
    for device in devices:
        print(device.respond())

    # Generate waveform
    visualizer = I2CSignalVisualizer()
    visualizer.plot_signals(devices)
