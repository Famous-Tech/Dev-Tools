#!/bin/bash

# Function to log messages with timestamps
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Check if Buildozer is installed
log "Checking for Buildozer..."
if ! command -v buildozer &> /dev/null; then
    log "Error: Buildozer is not installed. Please install it and try again."
    exit 1
fi

# Create the lib directory if it doesn't exist
log "Creating lib directory..."
mkdir -p lib

# Navigate to the devtools directory
log "Navigating to the devtools directory..."
cd devtools || { log "Error: devtools directory not found."; exit 1; }

# Clean any previous build artifacts
log "Cleaning previous build artifacts..."
buildozer android clean
if [ $? -ne 0 ]; then
    log "Error: Failed to clean previous build artifacts."
    exit 1
fi

# Build the APK
log "Building the APK..."
buildozer android release
if [ $? -ne 0 ]; then
    log "Error: APK build failed."
    exit 1
fi

# Find and move the APK to the lib directory
log "Moving APK to the lib directory..."
APK_PATH=$(find . -type f -name "*.apk" | head -n 1)
if [ -z "$APK_PATH" ]; then
    log "Error: APK not found."
    exit 1
fi

mv "$APK_PATH" ../lib/
if [ $? -eq 0 ]; then
    log "APK successfully compiled and moved to the lib directory."
else
    log "Error: Failed to move APK."
    exit 1
fi
