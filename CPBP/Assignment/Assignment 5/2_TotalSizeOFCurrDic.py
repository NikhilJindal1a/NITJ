# 2. Write a Program that computes total size of all the files in your current directory folder.

import os
# Compute total size of files in current directory
total_size = 0
files = os.listdir('.')  # List all items in current directory

for file in files:
    if os.path.isfile(file):
        total_size += os.path.getsize(file)

print("Total size of all files in the current directory:", total_size, "bytes")
