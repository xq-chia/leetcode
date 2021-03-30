"""
1. Initiate head to the 1st item(index: 0) of the list
2. Compare it to the item next to it
3. If the nth item is greater than (n+1)th item, swap them
4. Advance head to the next
5. Repeat the comparison until reaches the last(n-k)th item in the list
6. Repeat the entire process until k = n

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
