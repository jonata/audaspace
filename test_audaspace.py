#!/usr/bin/env python3
"""
Test script for audaspace functionality.
This script tests basic audaspace operations like creating devices and signals.
"""

import sys
import time
import os

def test_basic_functionality():
    """Test basic audaspace functionality"""
    print("Testing basic audaspace functionality...")
    
    try:
        import aud
        print("✓ Successfully imported aud module")
    except ImportError as e:
        print(f"✗ Failed to import aud module: {e}")
        return False

    # Test creating a device
    try:
        device = aud.Device()
        print("✓ Successfully created aud.Device()")
        print(f"  - Device sample rate: {device.rate}")
        print(f"  - Device channels: {device.channels}")
    except Exception as e:
        print(f"✗ Failed to create aud.Device(): {e}")
        return False

    # Test creating basic signals
    try:
        # Test sine wave
        sine = aud.Sound.sine(440)  # A4 note
        print("✓ Successfully created sine wave at 440Hz")
        
        # Test square wave (from sine with threshold)
        square = sine.threshold()
        print("✓ Successfully created square wave from sine")
        
        # Test other generators
        silence = aud.Sound.silence()
        print("✓ Successfully created silence")
        
        sawtooth = aud.Sound.sawtooth(220)
        print("✓ Successfully created sawtooth wave at 220Hz")
        
        triangle = aud.Sound.triangle(330)
        print("✓ Successfully created triangle wave at 330Hz")
        
    except Exception as e:
        print(f"✗ Failed to create signals: {e}")
        return False

    # Test playing a sound (briefly)
    try:
        print("Playing sine wave for 1 second...")
        handle = device.play(sine)
        time.sleep(1)
        handle.stop()
        print("✓ Successfully played sine wave")
    except Exception as e:
        print(f"✗ Failed to play sound: {e}")
        # This might fail in headless environments, so we'll continue

    # Test sound effects
    try:
        # Test volume effect
        vol_sound = sine.volume(0.5)
        print("✓ Successfully applied volume effect")
        
        # Test pitch effect
        pitch_sound = sine.pitch(1.5)
        print("✓ Successfully applied pitch effect")
        
        # Test loop effect
        loop_sound = sine.loop(2)  # Loop twice
        print("✓ Successfully applied loop effect")
        
    except Exception as e:
        print(f"✗ Failed to apply sound effects: {e}")
        return False

    # Test handle functionality
    try:
        handle = device.play(sine)
        print(f"✓ Successfully created playback handle")
        print(f"  - Handle is valid: {handle.valid}")
        print(f"  - Handle is playing: {handle.playing}")
        handle.stop()
        print("✓ Successfully stopped playback via handle")
    except Exception as e:
        print(f"✗ Failed to test handle functionality: {e}")
        # This might fail in headless environments

    print("
✓ Basic functionality test completed successfully!")
    return True


def test_advanced_functionality():
    """Test advanced audaspace functionality"""
    print("
Testing advanced audaspace functionality...")
    
    try:
        import aud
        
        # Test sequence functionality
        sequence = aud.Sequence()
        print("✓ Successfully created sequence")
        
        # Test sound mixing
        sine1 = aud.Sound.sine(440)
        sine2 = aud.Sound.sine(550)
        mixed = sine1.mix(sine2)
        print("✓ Successfully mixed two sounds")
        
        # Test effects
        delayed = sine1.delay(0.5)  # 0.5 second delay
        print("✓ Successfully applied delay effect")
        
        if hasattr(aud.Sound, "fadein") and hasattr(aud.Sound, "fadeout"):
            faded = sine1.fadein(0.5).fadeout(0.5)
            print("✓ Successfully applied fade in/out effects")

    except Exception as e:
        print(f"✗ Advanced functionality test failed: {e}")
        return False

    print("✓ Advanced functionality test completed successfully!")
    return True


def main():
    """Main test function"""
    print("Audaspace Test Suite")
    print("=" * 50)
    
    success = True
    
    # Test basic functionality
    success &= test_basic_functionality()
    
    # Test advanced functionality
    success &= test_advanced_functionality()
    
    print("
" + "=" * 50)
    if success:
        print("✓ All tests passed!")
        return 0
    else:
        print("✗ Some tests failed!")
        return 1


if __name__ == "__main__":
    sys.exit(main())
