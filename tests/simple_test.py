import aud
import time
import sys

print("Running audaspace simple test...")

try:
    print("Creating device...")
    # In a CI environment, a real audio device might not be available.
    # We try to use the "dummy" device as a fallback.
    device = aud.Device("dummy")
except Exception as e:
    print(f"Failed to create dummy aud.Device(): {e}", file=sys.stderr)
    sys.exit(1)

print("Device created successfully.")

try:
    print("Creating a sine wave sound...")
    sound = aud.Sine(440)
except Exception as e:
    print(f"Failed to create aud.Sine(440): {e}", file=sys.stderr)
    sys.exit(1)

print("Sound created successfully.")

try:
    print("Playing sound...")
    handle = device.play(sound)
except Exception as e:
    print(f"Failed to play sound: {e}", file=sys.stderr)
    sys.exit(1)

print("Sound is playing.")

# Let it play for a bit
time.sleep(0.5)

handle.stop()
print("Sound stopped.")

print("Test finished successfully!")
