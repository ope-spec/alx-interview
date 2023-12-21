#!/usr/bin/python3
"""Log parsing"""
import sys


def print_stats(total_size, status_codes):
    """
    Print statistics including total file size and
    number of lines for each status code.
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_codes):
        print("{}: {}".format(code, status_codes[code]))


def process_line(line, total_size, status_codes):
    """
    Process a log entry line, update total file size and status code counts.
    """
    try:
        parts = line.split()
        if len(parts) == 9:
            status_code = int(parts[-2])
            file_size = int(parts[-1])
            total_size += file_size
            if status_code in {200, 301, 400, 401, 403, 404, 405, 500}:
                if status_code not in status_codes:
                    status_codes[status_code] = 1
                else:
                    status_codes[status_code] += 1
        return total_size, status_codes
    except ValueError:
        return total_size, status_codes


def main():
    """
    Main function to read stdin line by line,
    compute metrics, and print statistics.
    """
    total_size = 0
    status_codes = {}
    line_count = 0

    try:
        for line in sys.stdin:
            line = line.strip()
            total_size, status_codes = process_line(
                line,
                total_size,
                status_codes
                )
            line_count += 1

            if line_count == 10:
                print_stats(total_size, status_codes)
                line_count = 0

    except KeyboardInterrupt:
        pass

    print_stats(total_size, status_codes)


if __name__ == "__main__":
    main()
