#!/bin/bash

# Function to log messages
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Function to check the last command status
check_status() {
    if [ $? -ne 0 ]; then
        log "Error: $1 failed."
        exit 1
    fi
}

# Step 1: Create the lib directory if it doesn't exist
log "Creating lib directory..."
mkdir -p lib
check_status "Creating lib directory"

# Step 2: Clean the project
log "Cleaning the project..."
./gradlew clean
check_status "Project cleaning"

# Step 3: Compile and build the APK
log "Building the APK..."
./gradlew assembleRelease
check_status "APK build"

# Step 4: Move the APK to the lib directory
log "Locating the APK..."
APK_PATH=$(find . -type f -name "*.apk" | grep release)
if [ -z "$APK_PATH" ]; then
    log "Error: APK not found."
    exit 1
fi

log "Moving APK to the lib directory..."
mv "$APK_PATH" lib/
check_status "Moving APK"

# Step 5: Final confirmation
log "APK successfully compiled and moved to the lib directory."
