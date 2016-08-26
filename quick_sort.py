"""Implementation of the quicksort algorithm to sort an array"""

import sys
import os.path

def quick_sort(filename):
    a = [int(x.strip()) for x in open(filename)] # Converting to integers  
    n = len(a)
    
    q_sort(a, 0, len(a)) # Calling the recursive algorithm
    
    return a


def q_sort (a, l, r):
    # This operates on a subset of array a with l the lower bound and r the
    # upper bound

    n = r - l + 1
    # In the case that the array is only one element, then it is simply returned
    if (n == 0) or (n == 1): 
        return

    # If the array is longer than one element, then it needs to be partitioned
    else: 
        pivot = partition(a, l, r)
        q_sort(a, l, pivot)
        q_sort(a, pivot+1, r)
    return


def partition (a, l, r):
    # A subroutine to partition portion l to r (where l and r are indices) of an
    # array a, about its first element
    pivot = a[l]
    i = l+1
    # Go through the array, and if the element is less than the pivot, swap it
    # with the leftmost element of the scanned elements that are greater than
    # the pivot
    for j in range (l+1, r):
        # Note that if a[j] > pivot, then nothing needs to be done
        if a[j] < pivot:
            temp = a[i]
            a[i] = a[j]
            a[j] = temp
            i+=1
    # Swapping the pivot into it's rightful place
    temp = a[l]
    a[l] = a[i-1]
    a[i-1] = temp

    # Returning the index position of the pivot
    return i-1


if __name__ == "__main__":
    if len(sys.argv) > 1:
        # An argument has been given, check if it is a valid file
        if os.path.isfile(sys.argv[1]):
            print "Running with file:", sys.argv[1]
            try:
                sorted_file = quick_sort(sys.argv[1])
                print "Sorted file:", sorted_file
            except:
                print "Error: Please provide a file with one integer per line"                
        # If an invalid argument is given, print an error message
        else:
            print >> sys.stderr, "Usage: {} <filename>".format(sys.argv[0])
            sys.exit(2)
    else:
        # No arguments given, run with a test file
        testfile = "sort_file.txt"
        print "Running with test file:", testfile
        print "Sorted file:", quick_sort(testfile)


