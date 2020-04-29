# partition method would change the order of array as well
def HoarePartition(A, lo, hi):
    i = lo
    j = hi
    p = A[lo]
    while i < j:
        while i < hi and A[i] <= p:
            i += 1
        while j >= lo and A[j] > p:
            j -= 1
        A[i], A[j] = A[j], A[i]
    A[i], A[j] = A[j], A[i]
    A[lo], A[j] = A[j], A[lo]
    return j

def test():
    A = [5,8,6,3,7,2,1]
    print(HoarePartition(A, 0, len(A)-1))
if __name__ == "__main__":
    test()