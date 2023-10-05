#!/bin/bash

# Check if at least 6 arguments are provided (program name + 5 arguments)
if [ "$#" -lt 8 ]; then
    echo "Usage: $0 <executable_file> <input_file> <output_file> <mnr> <mnc> <thr> <rk> <ck>"
    exit 1
fi

# Extract the program name and remove it from the argument list
program_name="$1"
shift

# Check if the program exists
if [ ! -x "$program_name" ]; then
    echo "Error: The program '$program_name' does not exist or is not executable."
    exit 1
fi

# Execute the program with the remaining arguments
"$program_name" "$@"