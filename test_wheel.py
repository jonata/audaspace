#!/usr/bin/env python3
"""Test script to verify audaspace wheel installation and functionality."""

import sys

def main():
    # Test 1: Import
    try:
        import aud
        import numpy as np
        print("✓ Successfully imported audaspace and numpy")
    except ImportError as e:
        print(f"✗ Import failed: {e}")
        return 1

    # Test 2: Create device
    try:
        device = aud.Device()
        print("✓ Device created successfully")
    except Exception as e:
        print(f"✗ Device creation failed: {e}")
        return 1

    # Test 3: Generate and play a simple tone
    try:
        duration = 0.1
        sample_rate = 44100
        frequency = 440.0
        
        t = np.linspace(0, duration, int(sample_rate * duration), False)
        samples = np.sin(2 * np.pi * frequency * t).astype(np.float32)
        
        sound = aud.Sound.buffer(samples, sample_rate)
        print("✓ Sound buffer created")
        
        handle = device.play(sound)
        handle.stop()
        print("✓ Sound playback test passed")
    except Exception as e:
        print(f"✗ Sound playback test failed: {e}")
        return 1

    # Test 4: Sequence
    try:
        seq = aud.Sequence()
        seq.add(sound, 0, 0, -1)
        print("✓ Sequence test passed")
    except Exception as e:
        print(f"✗ Sequence test failed: {e}")
        return 1

    # Test 5: Generators (if available)
    try:
        if hasattr(aud, 'Sine'):
            sine = aud.Sine(440)
            print("✓ Sine generator created")
        if hasattr(aud, 'Silence'):
            silence = aud.Silence()
            print("✓ Silence generator created")
        print("✓ Generator test passed")
    except Exception as e:
        print(f"✗ Generator test failed: {e}")
        return 1

    print("\n=== All tests passed! ===")
    return 0

if __name__ == "__main__":
    sys.exit(main())
