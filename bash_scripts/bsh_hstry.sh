#!/bin/bash
# bsh_hstry.sh

# Get current date and time
current_date=$(date "+%Y-%m-%d %H:%M:%S")

# File to store the history
output_file="./bash_scripts/bsh_cli_hstry"

# Write header to the file
echo "History exported on $current_date:" >> "$output_file"
echo "-----------------------" >> "$output_file"

# Append history to the file
history | cut -c 8- >> "$output_file"

# Add a newline for separation of entries
echo "" >> "$output_file"
