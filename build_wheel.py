#!/usr/bin/env python3
"""
Build script for audaspace Python wheel with bundled dependencies.
This script ensures all C++ libraries are properly linked and bundled.
"""
import os
import sys
import subprocess
import shutil
from pathlib import Path


def run_command(cmd, cwd=None, env=None):
    """Run a command and print output."""
    print(f"Running: {' '.join(cmd)}")
    result = subprocess.run(cmd, cwd=cwd, env=env, capture_output=False)
    if result.returncode != 0:
        print(f"Command failed with code {result.returncode}")
        sys.exit(result.returncode)
    return result


def build_wheel(platform_specific=True):
    """Build the wheel with all dependencies bundled."""
    root_dir = Path(__file__).parent.absolute()
    
    # Set environment variables for the build
    env = os.environ.copy()
    
    # Platform-specific settings
    if sys.platform == "linux":
        env["WITH_PULSEAUDIO"] = "ON"
        env["WITH_PIPEWIRE"] = "ON"
        env["WITH_JACK"] = "ON"
    elif sys.platform == "darwin":
        env["WITH_COREAUDIO"] = "ON"
        env["MACOSX_DEPLOYMENT_TARGET"] = "10.15"
    elif sys.platform == "win32":
        env["WITH_WASAPI"] = "ON"
    
    # Clean previous builds
    build_dir = root_dir / "build"
    if build_dir.exists():
        print(f"Cleaning {build_dir}")
        shutil.rmtree(build_dir)
    
    dist_dir = root_dir / "dist"
    if dist_dir.exists():
        print(f"Cleaning {dist_dir}")
        shutil.rmtree(dist_dir)
    
    # Build the wheel
    print("\n=== Building wheel ===")
    run_command([sys.executable, "-m", "pip", "install", "-v", "--no-build-isolation", "."], cwd=root_dir, env=env)
    
    print("\n=== Creating wheel package ===")
    run_command([sys.executable, "-m", "build", "--wheel", "--no-isolation"], cwd=root_dir, env=env)
    
    # Show built wheels
    if dist_dir.exists():
        wheels = list(dist_dir.glob("*.whl"))
        if wheels:
            print("\n=== Built wheels ===")
            for wheel in wheels:
                size = wheel.stat().st_size / (1024 * 1024)
                print(f"  {wheel.name} ({size:.2f} MB)")
        else:
            print("\nNo wheels found in dist/")
    
    return 0


if __name__ == "__main__":
    sys.exit(build_wheel())
