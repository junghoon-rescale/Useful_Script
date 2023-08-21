#################################################################################
#   Author: junghoon@rescale.com                                                #
#   Last updated: Aug 21, 2023                                                  #
#   Decrtiption: 
#   How to use: 
#################################################################################

import re
import sys
from datetime import datetime

# Check if the correct number of arguments is provided
if len(sys.argv) != 2:
    print("Usage: python script_name.py log_file_path")
    sys.exit(1)

log_file_path = sys.argv[1]

# Open the log file for reading
with open(log_file_path, 'r') as log_file:
    lines = log_file.readlines()

# Define regular expressions for timestamps and events
timestamp_pattern = r'\[(.*?)\]'
launching_pattern = r'^\[.*\]: Launching'
exited_pattern = r'^\[.*\]: Exited'

launching_timestamps = []
exited_timestamps = []

# Iterate through each line in the log file
for line in lines:
    timestamp_match = re.search(timestamp_pattern, line)
    if timestamp_match:
        timestamp = timestamp_match.group(1)
        if re.search(launching_pattern, line):
            launching_timestamps.append(datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%SZ'))
        elif re.search(exited_pattern, line):
            exited_timestamps.append(datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%SZ'))

# Calculate and print the running time for each job
for launch_time, exit_time in zip(launching_timestamps, exited_timestamps):
    running_time = (exit_time - launch_time).total_seconds()
    print(f"Running time: {running_time:.2f} seconds")
