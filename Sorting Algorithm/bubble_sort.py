"""
Time Complexity:    O(n^2)
Space Complexity:   O(1)

List is looped through twice in all cases, O(n^2)
No extra spaces are allocated in all cases, O(1)

Stable Sorting Algorithm, In-place Sorting Algorithm
"""
def bubble(n:list) -> list:
    for i in range(len(n)):
        for head in range(len(n) - i - 1):
            if n[head] > n[head + 1]:
                n[head], n[head + 1] = n[head + 1], n[head]
    return n

"""
Time Complexity:    O(n^2)
Space Complexity:   O(1)

List is looped through once in best case scenario, O(n)
List is looped through twice in worst case scenario, O(n^2)
No extra spaces are allocated in all cases, O(1)

Stable Sorting Algorithm, In-place Sorting Algorithm
"""
def bubble_optimised(n:list) -> list:
    for i in range(len(n)):
        swapped = False
        for head in range(len(n) - i - 1):
            swapped = True
            if n[head] > n[head + 1]:
                n[head], n[head + 1] = n[head + 1], n[head]
        if (!swapped):
            break
    return n
