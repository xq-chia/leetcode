"""
Time Complexity: O(n^2)
Space Complexity: O(1)

List is looped through once in best case scenario, O(n)
List is looped through twice in worst case scenario, O(n^2)
Only one space is allocated, temp, in all cases, O(1)

Stable Sorting Algorithm, In-place Sorting Algorithm
"""

def insertion(n:list) -> list:
    for tail in range(1, len(n)):
        head = tail - 1
        temp = n[tail]
        while head >= 0 and temp < n[head]:
            n[head + 1] = n[head]
            head -= 1
        n[head + 1] = temp
    return n
