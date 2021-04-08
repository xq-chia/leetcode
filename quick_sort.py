"""
Time Complexity:    O(nlog(n))
Space Complexity:   O(log(n))

Unstable Sorting Algorithm, In-place Sorting Algorithm
"""
def quick_sort(n:list, left:int, right:int) -> list:
    def partition(n:list, left: int, right:int) -> int:
        pivot = n[left]
        i, j = left + 1, right
        while True:
            while i <= j and n[i] <= pivot:
                i += 1
            while j >= i and n[j] >= pivot:
                j -= 1
            if i >= j:
                break
            n[i], n[j] = n[j], n[i]
        n[left], n[j] = n[j], pivot
        return j

    if left < right:
        mid = partition(n, left, right)
        quick_sort(n, left, mid - 1)
        quick_sort(n, mid + 1, right)
    return n
