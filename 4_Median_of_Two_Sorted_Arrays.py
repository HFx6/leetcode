import math
import statistics
def findMedianSortedArrays(nums1, nums2) -> float:
    master = [*nums1, *nums2]
    master.sort()
    return statistics.median(master)