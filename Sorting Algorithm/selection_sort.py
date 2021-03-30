"""
1. Find the smallest integer in the list
2. Swap the smallest integer with the head of the list
3. Advance the head of the list to the next

Time Complexity:    O(n^2)
Space Complexity:   O(1)

List is looped through twice in all cases, O(n^2)
No extra spaces are required, O(1)

Unstable Sorting Algorithm, In-place Sorting Algorithm
"""
def selection(n:list) -> list:
    for head in range(len(n)):
        smallest = head
        for i in range(head + 1, len(n)):
            smallest = i if n[i] < n[smallest] else smallest
        n[head], n[smallest] = n[smallest], n[head]
    return n
