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

        # Skip the header if input is the first line.
        if line[0] == "id":
            continue

        # Filter all input data where the node is a question type.
        if line[5] == "question":

            # Get the tags, then strip and split white space.
            tags = line[2].strip().split()

            # Print each word and a value of 1.
            for i in tags:
                print "{0}\t{1}".format(i.lower(), "1")

if __name__ == "__main__":
    sys.stdin = sys.stdin.readlines()
    mapper()
