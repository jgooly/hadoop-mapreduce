#!/usr/bin/python

'''
    Author: Julian Ganguli
    Date created: 12/20/2016
    Python Version: 2.7
'''

import sys


def reducer():
    # Initialize variables.

    currentQuestionKey = None
    studentList = []

    for line in sys.stdin:
        data = line.strip().split("\t")

        # Skip line if something has gone wrong.
        if len(data) != 2:
            continue

        # Map data to explicit variables.
        newQuestionKey, newStudentKey = data

        # If the new key differs from the current key, send student list to stdout.
        if currentQuestionKey and currentQuestionKey != newQuestionKey:
            print currentQuestionKey, studentList
            studentList = []  # Reset to empty list for the new key.

        currentQuestionKey = newQuestionKey

        # Append student to list.
        studentList.append((newStudentKey))

    # Send last key, values to stdout.
    if currentQuestionKey is not None:
        print currentQuestionKey, studentList


if __name__ == "__main__":
    sys.stdin = sys.stdin.readlines()
    reducer()
