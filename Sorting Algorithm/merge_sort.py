"""
Time Complexity:   O(nlog(n)) 
Space Complexity:   O(n)

Recursive Algorithm
Stable Sorting Algorithm, Out-of-place Sorting Algorithm
"""
def merge_sort(n:list, left:int, right:int) -> list:
    def merge_list(n:list, left:int , mid:int, right:int) -> list:
        i, j = left, mid + 1
        temp = list()

        while (i <= mid and j <= right):
            if (n[i] < n[j]):
                temp.append(n[i])
                i += 1
            else:
                temp.append(n[j])
                j += 1
        while (i <= mid):
            temp.append(n[i])
            i += 1
        while (j <= right):
            temp.append(n[j])
            j += 1

        for i in range(0, len(temp)):
            n[left] = temp[i]
            left += 1
        return n

    if left < right:
        mid = (left + right) // 2

        merge_sort(n, left, mid)
        merge_sort(n, mid + 1, right)
        merge_list(n, left, mid, right)
    return n
