"""Implementation of the median maintenance algorithm. Given a file containing
the integers 1 to 10000 in unsorted order, treat this as a stream of numbers.
Compute and add the median as each new number arrives to a running total."""

import copy
import math
import heapq
import sys
import os.path

def median_maintenance(filename):

    data = [int(x) for x in open(filename)] 
    
    # Initialise an empty heap for the smallest half of the numbers
    heapsmall = []
    # Initialise an empty heap for the largest half of the numbers
    heapbig = []
    # Initialising the sum of the medians to be zero
    mediansum = 0
    lastmedian = 0

    # Take each integer in turn from the data list
    for item in data:
        # For each integer, if it is smaller than the current median, put it
        # in the small number heap, if it is larger than or the same as the
        # current median, put it in the big number heap. If it goes in the
        # small number heap, the sign must be reversed so that the maximum of
        # these values can easily be found
        if (item < lastmedian):
            heapq.heappush(heapsmall, -item)
        else:
            heapq.heappush(heapbig, item)
        # Check that the arrays are of equal size, if there is an odd number,
        # the extra number should be in the array of smaller numbers, so
        # readjust the size of the arrays
        if (len(heapbig) == (len(heapsmall) + 1)):
            x = heapq.heappop(heapbig)
            heapq.heappush(heapsmall, -x)
        elif (len(heapsmall) == (len(heapbig) + 2)):
            x = heapq.heappop(heapsmall)
            heapq.heappush(heapbig, -x)

        # If the arrays are the same size, average the smallest value from the
        # array of largger values and the largest value from the array of
        # smaller values. Otherwise, read the largest value from the array of
        # smaller numbers (this array is always maintained as being the same
        # size or one bigger than the array of bigger numbers). Note that the
        # sign on the value from the array of smaller numbers must be reversed.
        if len(heapbig) == len(heapsmall):
            lastmedian = 0.5 * (-(heapsmall[0]) + (heapbig[0]))
        else:
            lastmedian = -(heapsmall[0])
        #lastmedian = -(heapsmall[0])
        mediansum += lastmedian

    return mediansum


if __name__ == "__main__":
    if len(sys.argv) > 1:
        # An argument has been given, check if it is a valid file
        if os.path.isfile(sys.argv[1]):
            print "Running with file:", sys.argv[1]
            try:
                mediansum = median_maintenance(sys.argv[1])
                print "Sum of the medians:", mediansum
            except:
                print "Error: Please provide a file with one integer per line"                
        # If an invalid argument is given, print an error message
        else:
            print >> sys.stderr, "Usage: {} <filename>".format(sys.argv[0])
            sys.exit(2)
    else:
        # No arguments given, run with a test file
        testfile = "median_maintenance_file.txt"
        print "Running with test file:", testfile
        print "Sum of the medians:", median_maintenance(testfile)
