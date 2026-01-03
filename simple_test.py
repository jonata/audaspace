import aud
print("Testing audaspace import...")
device = aud.Device()
print(f"Device created: {device}")
sine = aud.Sound.sine(440)
print(f"Sine wave created: {sine}")
print("Basic functionality test passed!")
