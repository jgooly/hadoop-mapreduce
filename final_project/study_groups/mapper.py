#!/usr/bin/python

'''
    Author: Julian Ganguli
    Date created: 12/20/2016
    Python Version: 2.7
'''

import sys
import csv


def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')

    for line in reader:

        # Skip the header (first row of data).
        if line[0] == "id":
            continue

        # Send the needed ids for questions, answers, or comments to stdout.
        else:
            # if line[5] == "answer" or line[5] == "comment":
            if line[5] in ["answer", "comment"]:
                print line[7], "\t", line[3]
            if line[5] == "question":
                print line[0], "\t", line[3]


if __name__ == "__main__":
    sys.stdin = sys.stdin.readlines()
    mapper()
