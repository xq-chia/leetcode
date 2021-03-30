"""
1. Initiate head to the 2nd item(index: 1) in the list
2. Compare head with (n-1)th item.
   a. If head is smaller than (n-1)th item, compare it with (n-2)th item
   b. Else push (n-k)th item to (n-1)th item to the left and insert head at (n-k)th position
3. Advance head to the next

Time Complexity: O(n^2)
Space Complexity: O(1)

List is looped through once in best case scenario, O(n)
List is looped through twice in worst case scenario, O(n^2)
Only one space is allocated, temp, in all cases, O(1)

Stable Sorting Algorithm, In-place Sorting Algorithm
"""
def insertion(n:list) -> list:
    for head in range(1, len(n)):
        tail = head - 1
        temp = n[head]
        while tail >= 0 and temp < n[tail]:
            n[tail + 1] = n[tail]
            tail -= 1
        n[tail + 1] = temp
    return n
print(insertion([3,5,2,8,6,4,1,7,9]))
