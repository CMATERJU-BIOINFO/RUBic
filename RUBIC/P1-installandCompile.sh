#!/bin/bash

# Check if the correct number of arguments is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <c_source_file>"
    exit 1
fi

# Check if GCC is installed
if ! command -v gcc &> /dev/null; then
    echo "GCC is not installed. Installing GCC..."
    sudo apt-get update
    sudo apt-get install -y gcc
fi

# Get the source file name from the command line argument
source_file="$1"

# Extract the base name of the source file (without the .c extension)
base_name=$(basename "$source_file" .c)

# Compile the C program and create an executable file
gcc "$source_file" -o "$base_name" -lm

# Check if compilation was successful
if [ $? -eq 0 ]; then
    echo "Compilation successful. Executable file created: $base_name"
else
    echo "Compilation failed."
fi

