#!/usr/bin/env python
"""Test script to verify audaspace wheel installation and functionality."""

import sys
import aud
import numpy as np

def main():
    print('✓ Successfully imported audaspace')
    print(f'  Module location: {aud.__file__}')

    # Test 1: Create device
    try:
        device = aud.Device()
        print('✓ Device created successfully')
    except Exception as e:
        print(f'✗ Device creation failed: {e}')
        return 1

    # Test 2: Generate and play a tone
    try:
        duration = 0.1
        sample_rate = 44100
        frequency = 440.0
        
        # Generate a sine wave
        t = np.linspace(0, duration, int(sample_rate * duration), False)
        samples = np.sin(2 * np.pi * frequency * t).astype(np.float32)
        
        # Create sound buffer
        sound = aud.Sound.buffer(samples, sample_rate)
        print('✓ Sound buffer created')
        
        # Play sound
        handle = device.play(sound)
        handle.stop()
        print('✓ Sound playback test passed')
    except Exception as e:
        print(f'✗ Sound playback test failed: {e}')
        return 1

    # Test 3: Create sequence
    try:
        seq = aud.Sequence()
        seq.add(sound, 0, 0, -1)
        print('✓ Sequence test passed')
    except Exception as e:
        print(f'✗ Sequence test failed: {e}')
        return 1

    # Test 4: Test various sound generators
    try:
        sine = aud.Sine(440)
        print('✓ Sine generator created')
        
        silence = aud.Silence()
        print('✓ Silence generator created')
    except Exception as e:
        print(f'✗ Generator test failed: {e}')
        return 1

    print('\n=== All tests passed! ===')
    return 0

if __name__ == '__main__':
    sys.exit(main())
