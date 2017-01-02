#!/usr/bin/python

'''
    Author: Julian Ganguli
    Date created: 12/20/2016
    Python Version: 2.7
'''

import sys


def reducer():
    # Initialize variables.
    currId, currType = None, None
    avgAnsLength, ansCount, bodyLenTotal, questionLength = 0, 0, 0, 0

    # Split on white space. Map the id, post type, and body length variables.
    for line in sys.stdin:
        thisID = line.split(' ')[0]
        thisType = line.split(' ')[1]
        bodyLength = int(line.split("\t")[1])

        # If the id has changed, then output the results and reset variables.
        if currId and currId != thisID:
            print currId, "\t", questionLength, "\t", avgAnsLength
            currId = thisID
            currType = thisType
            avgAnsLength, ansCount, bodyLenTotal, questionLength = 0, 0, 0, 0

        currId = thisID
        currType = thisType

        # Check the post type and calculate the new average if the post type is an 'answer'.

        if currType == "A":
            ansCount += 1
            bodyLenTotal += bodyLength
            avgAnsLength = float(bodyLenTotal / ansCount)

        # If the post type is a question, then set the question length variable to the body length value.
        # This operation should only happen once for each id.
        if currType == "Q":
            questionLength = bodyLength

    # print last set of values
    if currId != None:
        print currId, "\t", questionLength, "\t", avgAnsLength


if __name__ == "__main__":
    sys.stdin = sys.stdin.readlines()
    reducer()
