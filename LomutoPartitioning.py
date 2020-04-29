# find the partition in the unsorted array (choose the first position as pivot)
def LomutoPartition(A, lo, hi):
    p = A[lo]
    s = lo
    for i in range(lo+1, hi+1) :
        if (A[i] < p) :
            s += 1
            A[s], A[i] = A[i], A[s]
    #         temp1 = A[s]
    #         A[s] = A[i]
    #         A[i] = temp1
    A[lo], A[s] = A[s], A[lo]
    # temp2 = A[0]
    # A[0] = A[s]
    # A[s] = temp2
    return s

def test():
    A = [7,3,4,8,10,9]

    # Order of array A would be modified
    print(LomutoPartition(A, 0, 5))
    print(A)
if __name__ == "__main__" :
    test()

