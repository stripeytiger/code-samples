"""Program which uses the divide and conquer method to count the inversions
in an array of numbers (note that an inversion is when any pair of numbers is
out of sequence, and is counted for every individual pair). This piggybacks on
the merge_sort algorithm.
"""

import sys
import os.path

def count_inversions(filename):
    a = [int(x.strip()) for x in open(filename)] # Converting to integers  

    d, count = split_and_merge(a)
    return d, count # Return the sorted array and the count


def split_and_merge (a):
    # Recursive algorithm for the split and merge
    n = len(a)

    # If the array has only one element, then it is simply returned with 0
    # inversions
    if n == 1:
        return a, 0

    # In the case that the array is two elements, they need to be sorted into
    # ascending order and returned
    elif n == 2: 
        if a[0] > a[1]:
            return [a[1], a[0]], 1 # There is an inversion, so return 1
        else:
            return a, 0 # There is no inversion, so return 0

    # If the array is longer than two elements, it needs to be split in two,
    # and the split_and_merge function recursively called on each half
    else: 
        m = (n/2)
        b = a[0:m]
        c = a[m:n]
        b, countb = split_and_merge(b)
        c, countc = split_and_merge(c)
        
    # When the array has been split down to 1- or 2-component elements, then
    # these are merged back together, starting from the smallest elements and
    # merging until the full array has been combined. The splits are counted.
    d, countd = merge_and_count(b, c)

    # Adding the left inversions, right inversions and split inversions together
    count = countb + countc + countd 
    
    return d, count


def merge_and_count(p, q):
    # Function to merge two arrays (which are already sorted into ascending
    # order) together into a single array of ascending order
    
    # Initialising indices to mark position in the p and q arrays
    pindex = qindex = 0 
    psize = len(p)
    qsize = len(q)
    # Initialising an array to hold the sorted array
    d = [0]*(psize+qsize)
    count = 0

    for k in range(psize+qsize):
        # Standard case, where there are still elements in both arrays
        if ((pindex < psize) and (qindex < qsize)):
            # Checking which of the leading numbers in the arrays is smaller,
            # and putting the lowest number in the output array. The relevant
            # index is incremented
            if p[pindex] < q[qindex]:
                d[k] = p[pindex]
                pindex+=1 # Incrementing the p index
            else:
                d[k] = q[qindex]
                qindex+=1 # Incrementing the q index
                count += psize - pindex

        # In the case that p is empty but there are still elements in q
        elif (qindex < qsize):
            # Checking which of the leading numbers in the arrays is smaller,
            # and putting the lowest number in the output array. The relevant
            # index is incremented
            d[k] = q[qindex]
            qindex+=1

        # In the case that q is empty but there are still elements in p
        elif (pindex < psize):
            # Checking which of the leading numbers in the arrays is smaller,
            # and putting the lowest number in the output array. The relevant
            # index is incremented
            d[k] = p[pindex]
            pindex+=1

    return d, count


if __name__ == "__main__":
    if len(sys.argv) > 1:
        # An argument has been given, check if it is a valid file
        if os.path.isfile(sys.argv[1]):
            print "Running with file:", sys.argv[1]
            try:
                sorted, countinv = count_inversions(sys.argv[1])
                print "Number of inversions:", countinv
            except:
                print "Error: Please provide a file with one integer per line"                
        # If an invalid argument is given, print an error message
        else:
            print >> sys.stderr, "Usage: {} <filename>".format(sys.argv[0])
            sys.exit(2)
    else:
        # No arguments given, run with a test file
        testfile = "count_inversions_file.txt"
        print "Running with test file:", testfile
        sorted, countinv = count_inversions(testfile)
        print "Number of inversions:", countinv
