#!/usr/bin/env python3
"""
Final test script for audaspace functionality.
This script tests basic audaspace operations like creating signals.
"""

def test_basic_functionality():
    """Test basic audaspace functionality"""
    print("Testing basic audaspace functionality...")
    
    try:
        import aud
        print("✓ Successfully imported aud module")
    except ImportError as e:
        print(f"✗ Failed to import aud module: {e}")
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

    print("✓ Basic functionality test completed successfully!")
    return True


def main():
    """Main test function"""
    print("Audaspace Final Test Suite")
    print("=" * 50)
    
    success = test_basic_functionality()

    print("\\n" + "=" * 50)
    if success:
        print("✓ All tests passed!")
        return 0
    else:
        print("✗ Some tests failed!")
        return 1


if __name__ == "__main__":
    import sys
    sys.exit(main())
