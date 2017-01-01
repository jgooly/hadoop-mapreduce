#!/usr/bin/python

'''
    Author: Julian Ganguli
    Date created: 12/20/2016
    Python Version: 2.7
'''

import sys
import csv


def reducer():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t')

    # Initialize variables.
    currentWord = None
    count = 0
    myList = []

    for line in reader:

        # Map data.
        thisWord, thisCount = line

        # If the key changes, then print output.
        if currentWord and currentWord != thisWord:

            # Handle cases where there are less than 10 unique words. Sort and print out all word, value tuples.
            if len(myList) < 10:
                myList.append((currentWord, count))
                myList.sort(key=lambda var: var[1])

            # Handles cases where there are more than 10 unique words.
            else:
                if count > myList[0][1]:
                    myList.pop(0)  # Since the list is sorted in ascending order, pop the first tuple.
                    myList.append((currentWord, count))  # Append the new word and count.
                    myList.sort(key=lambda x: x[1])  # Sort the list in ascending order by count.
            count = 0

        currentWord = thisWord
        count += 1

    # Block handles the last key since it doesn't change and is not caught in previous blocks.
    if currentWord is None:

        # Handles cases when there are less than 10 unique words.
        if len(myList) < 10:
            myList.append((currentWord, count))
            myList.sort(key=lambda var: var[1])
            myList.reverse()  # Sorting in descending order for final output.

        else:
            # Handle cases when there are more than 10 unique words.
            if myList[0][1] < count:
                myList.pop(0)
                myList.append((currentWord, count))
                myList.sort(key=lambda var: var[1])
                myList.reverse()  # Sorting in descending order for final output.

    # Print to final output.
    for tags in myList:
        writer.writerow(tags)


if __name__ == "__main__":
    sys.stdin = sys.stdin.readlines()
    reducer()
