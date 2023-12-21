#!/usr/bin/python3
"""script that reads stdin line by line and computes metrics"""
import sys

# Initialize a dictionary to store counts of different result codes
cache = {'200': 0, '301': 0, '400': 0, '401': 0,
         '403': 0, '404': 0, '405': 0, '500': 0}

# Initialize variables to track total file size and line count
total_size = 0
line_count = 0

try:
    # Iterate over each line from standard input
    for line in sys.stdin:
        # Split the line into a list of words
        line_list = line.split(" ")

        # Check if the line has the expected format
        if len(line_list) > 4:
            result_code = line_list[-2]
            size = int(line_list[-1])

            # Update the count for the result code in the dictionary
            if result_code in cache.keys():
                cache[result_code] += 1

            # Update total file size and line count
            total_size += size
            line_count += 1

        # Print statistics after every 10 lines
        if line_count == 10:
            line_count = 0
            print('File size: {}'.format(total_size))
            for key, value in sorted(cache.items()):
                if value != 0:
                    print('{}: {}'.format(key, value))

except Exception as err:
    # Ignore exceptions and continue to finally block
    pass

finally:
    # Print final statistics
    print('File size: {}'.format(total_size))
    for key, value in sorted(cache.items()):
        if value != 0:
            print('{}: {}'.format(key, value))
