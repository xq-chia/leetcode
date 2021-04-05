"""
Time Complexity: O(nlog(n))
Space Complexity: O(1)

Unstable Sorting Algorithm, In-place Sorting Algorithm
"""
def shell(n:list) -> list:
    interval = len(n) // 2
    while interval > 0:
        for tail in range(interval, len(n)):
            insertion(n, tail, interval)
        interval // 2
    return n

def insertion(n:list, tail:int, interval:int) -> list
    head = tail - interval
    temp = n[tail]
    while (head >= 0 and n[head] > temp):
        n[head + interval] = n[head]
        head -= interval
    n[head + interval] = temp
    return n
    
