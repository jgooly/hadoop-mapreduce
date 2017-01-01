#!/usr/bin/python

'''
    Author: Julian Ganguli
    Date created: 12/20/2016
    Python Version: 2.7
'''

import sys


def reducer():
    # Helper function.
    def max_out(listy):
        """
        Prints 1 or more keys and values. This function is a cleaner way iterate
        through a list and send the needed values to stdout.
        :param listy: A list of hour integers.
        :return: stdout student id and hour(s).
        """
        max_counts = max(listy)
        for i, j in enumerate(listy):
            if j == max_counts:
                print key, "\t", i

    # Initialize key to empty string.
    key = ""
    # Initialize empty list to store values.
    hours_list = [0] * 24

    for line in sys.stdin:
        data = line.strip().split("\t")

        # Something has gone wrong. Skip this line.
        if len(data) != 2:
            continue

        # Map data values.
        thisKey, thisHour = data

        # If the key changes, then print out the return values.
        if key and key != thisKey:
            max_out(hours_list)
            hours_list = [0] * 24  # Reset list for next key.

        hours_list[int(thisHour)] += 1  # Increment the array by 1.
        key = thisKey  # Reset the key.

    # This block prints out the values for the last line of input.
    if key != "":
        max_out(hours_list)


if __name__ == "__main__":
    sys.stdin = sys.stdin.readlines()
    reducer()
