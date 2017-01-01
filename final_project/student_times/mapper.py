#!/usr/bin/python

'''
    Author: Julian Ganguli
    Date created: 12/20/2016
    Python Version: 2.7
'''

import sys
import csv


def mapper():
    # Helper function.
    def get_hour(timestamp):
        """
        Returns the hour for a given timestamp input.
    
        :param timestamp: A timestamp (string).
        :return: the hour (int).
        """
        date, time = timestamp.split(' ')
        time_c, temp = time.split('.')
        return int(time_c[:2])

    reader = csv.reader(sys.stdin, delimiter='\t')

    # Read standard input line by line.
    for line in reader:
        if len(line) == 19 and line[0] != 'id':

            # Map needed values for reducer.
            a_id = line[3]
            try:
                hour = get_hour(line[8])
            except:  # Should be more defensive...
                pass

            print "{0}\t{1}".format(a_id, hour)


if __name__ == "__main__":
    sys.stdin = sys.stdin.readlines()
    mapper()
