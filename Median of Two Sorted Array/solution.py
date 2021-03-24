class Solution:
    def findMedianSortedArrays1(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Join and Median
        ---------------
        Time Complexity:    O(min(n, m))
        Space Complexity:   O(n + m)
        """

        def mergeList(nums1: List[int], nums2: List[int]) -> List[int]:
            ret = list()
            i, j = 0, 0

            while i < len(nums1) and j < len(nums2):
                if nums1[i] < nums2[j]:
                    ret.append(nums1[i])
                    i += 1
                else:
                    ret.append(nums2[j])
                    j += 1

            ret += nums1[i:] + nums2[j:]
            return ret
        
        nums3 = mergeList(nums1, nums2)
        lenght = len(nums3)

        if lenght % 2:
            return (nums3[lenght // 2])
        else:
            return (nums3[lenght // 2] + nums[(lenght // 2) - 1]) / 2

    def findMedianSortedArrays2(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Median without Join
        -------------------
        Time Complexity:    O(log(m + n))
        Space Complexity:   O(1)
        """

        nums1_len = len(nums1)
        nums2_len = len(nums2)
        total_len = nums1_len + nums2_len

        def getElement(n: int) -> int:
            index1_head, index2_head = 0, 0
            while True:
                if index1_head == nums1_len:
                    return nums2[index2_head + n - 1]
                if index2_head == nums2_len:
                    return nums1[index1_head + n - 1]
                if n == 1:
                    return min(nums1[index1_head], nums2[index2_head])

                index1 = min(index1_head + n // 2 - 1, nums1_len - 1)
                index2 = min(index2_head + n // 2 - 1, nums2_len - 1)
                nums1_num = nums1[index1]
                nums2_num = nums2[index2]

                if nums1_num < nums2_num:
                    n -= index1 - index1_head + 1
                    index1_head = index1 + 1
                else:
                    n -= index2 - index2_head + 1
                    index2_head = index2 + 1

        if (total_len % 2):
            return (getElement((total_len + 1) // 2))
        else:
            return (getElement(total_len // 2 + 1) + getElement(total_len // 2)) / 2

    def findMedianSortedArrays3(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Algorithm
        ---------
        Time Complexity:    O(log(min(m, n))) 
        Space Complexity:   O(1)
        """
        nums1_len = len(nums1)
        nums2_len = len(nums2)
        
        if nums1_len > nums2_len:
            return self.findMedianSortedArrays3(nums2, nums1)

        imin, imax = 0, nums1_len
        while imin <= imax:
            i = (imin + imax) / 2
            j = (nums1_len + nums2_len + 1) / 2 - i

            if i < nums1_len and nums2[j - 1] > nums1[i]:
                imin = i + 1
            elif i > 0 and nums1[i - 1] > nums2[j]:
                imax = i - 1
            else:
                if i == 0:
                    left_max = nums2[j - 1]
                elif j == 0:
                    left_max = nums1[i - 1]
                else:
                    left_max = max(nums1[i - 1], nums2[j - 1])

                if (nums1_len + nums2_len) % 2:
                    return left_max
                if i == nums1_len:
                    right_min = nums2[j]
                elif j == nums2_len:
                    right_min = nums1[i]
                else:
                    right_min = min(nums1[i], nums2[j])
                return (left_max + right_min) / 2
