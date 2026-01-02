################################################################################
# scikit-build-core configuration for audaspace Python module
# This file is included via AUDASPACE_CMAKE_CFG when building with scikit-build-core
# It provides minimal configuration changes without modifying the main CMakeLists.txt
################################################################################

message(STATUS "=== scikit-build-core configuration active ===")

# Disable the old setup.py-based Python module build
set(WITH_PYTHON_MODULE OFF CACHE BOOL "Disable setup.py build when using scikit-build-core" FORCE)

# Configure to build a proper Python extension module
# The main CMakeLists.txt will create audaspace-py, we'll make it install correctly
set(CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}" CACHE PATH "Install prefix" FORCE)

message(STATUS "scikit-build-core: Will build Python bindings and install to wheel")
