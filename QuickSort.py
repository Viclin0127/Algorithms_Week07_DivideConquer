# QuickSort method
# unstable
# in-place
# best O(nlogn)
# average case O(nlogn)   / O(1.39nlogn)  by Sedgewick/Wayne
# worst O(n^2) can be solved
# in this code, I use Hoare Partition method and Lomuto Partition method

from HoarePartition import HoarePartition
from LomutoPartitioning import LomutoPartition
import random

def QuickSort(A, lo, hi):
    if lo < hi:
        s = HoarePartition(A, lo, hi)
        QuickSort(A, lo, s-1)
        QuickSort(A, s+1, hi)

def test():
    A = [8,4,5,2,7,9,10]
    random.shuffle(A)           # shuffle an array to make closer to average case
    QuickSort(A, 0, len(A)-1)
    print(A)
if __name__ == "__main__":
    test()