#!/usr/bin/python

import sys

# Initialize variables.
oldID, oldTYpe = None, None
avgAnsLength, ansCount, bodyLenTotal, questionLength = 0, 0, 0, 0

# Split on white space. Map the id, post type, and body length variables.
for line in sys.stdin:
    thisID = line.split(' ')[0]
    thisType = line.split(' ')[1]
    bodyLength = int(line.split("\t")[1])

    # If the id has changed, then output the results and reset variables.
    if oldID and oldID != thisID:
        print oldID, "\t", questionLength, "\t", avgAnsLength
        oldID = thisID
        oldType = thisType
        avgAnsLength, ansCount, bodyLenTotal, questionLength = 0, 0, 0, 0

    oldID = thisID
    oldType = thisType

    # Check the post type and calculate the new average if the post type is an 'answer'.

    if oldType == "A":
        ansCount += 1
        bodyLenTotal += bodyLength
        avgAnsLength = float(bodyLenTotal / ansCount)
    # If the post type is a question, then set the question length variable to the body length value.
    # This operation should only happen once for each id.
    if oldType == "Q":
        questionLength = bodyLength

# print last set of values
if oldID != None:
    print oldID, "\t", questionLength, "\t", avgAnsLength
