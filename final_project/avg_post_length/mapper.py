#!/usr/bin/python

import csv
import sys


def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')

    for line in reader:

        # If input is the first line/header, skip it.
        if line[0] == "id":
            continue
        else:
            # Adding appropriate flag to each response category.

            # Check the node_type. If node_type == "answer", then map the parent_id, add flag, and body length.
            if line[5] == "answer":
                print line[7], "A", "\t", len(line[4])
            # Check the node_type. If node_type == "question", then map the id, add flag, and body length.
            if line[5] == "question":
                print line[0], "Q", "\t", len(line[4])


if __name__ == "__main__":
    sys.stdin = sys.stdin.readlines()
    mapper()
