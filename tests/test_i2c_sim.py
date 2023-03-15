from simulation.i2c_ack_sim import I2CDevice

def test_device_response():
    dev = I2CDevice(0x42)
    assert "ACK" in dev.respond()

def test_multiple_devices():
    addresses = [0x11, 0x22, 0x33]
    responses = [I2CDevice(a).respond() for a in addresses]
    assert len(responses) == 3
    assert all("ACK" in r for r in responses)
