class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        counter = 0
        for number in nums2:
            found = False
            while not found:
                if len(nums1) == counter:
                    nums1.append(number)
                    found = True
                elif number < nums1[counter]:
                    nums1.insert(counter,number)
                    found = True
                counter +=1
        return self.median(nums1)
    

    def median(self, nums1: List[int]):
        if len(nums1) % 2 == 1:
            return nums1[len(nums1)//2]
        else:
            return (nums1[(len(nums1)//2) - 1] + nums1[len(nums1)//2])/2