#!/usr/bin/python3
"""Log parsing"""
import sys

def process_line(line, cache, total_size, count):
    line_list = line.split(" ")
    if len(line_list) > 4:
        code = line_list[-2]
        size = int(line_list[-1])
        if code in cache:
            cache[code] += 1
        total_size += size
        count += 1
    return total_size, count

def print_stats(total_size, cache):
    print('File size: {}'.format(total_size))
    for key, value in sorted(cache.items()):
        if value != 0:
            print('{}: {}'.format(key, value))

def main():
    cache = {'200': 0, '301': 0, '400': 0, '401': 0,
             '403': 0, '404': 0, '405': 0, '500': 0}
    total_size = 0
    count = 0

    try:
        for line in sys.stdin:
            total_size, count = process_line(line, cache, total_size, count)
            if count == 10:
                count = 0
                print_stats(total_size, cache)

    except Exception as err:
        pass

    finally:
        print_stats(total_size, cache)

if __name__ == "__main__":
    main()
