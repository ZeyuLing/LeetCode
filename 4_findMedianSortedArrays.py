class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        p=0
        q=0
        array=[]
        total_len=len(nums1)+len(nums2)
        while p<len(nums1)and q<len(nums2):
            if(len(array)>(total_len/2)):break
            array.append(min(nums1[p],nums2[q]))
            if(nums1[p]<nums2[q]):p+=1
            else: q+=1
        while(p<len(nums1)):
            array.append(nums1[p])
            p+=1
        while(q<len(nums2)):
            array.append(nums2[q])
            q+=1
        if(total_len%2==1):
            return array[int(total_len/2)]
        else:
            return float(array[int(total_len/2)-1]+array[int(total_len/2)])/2       #leetcode编译器默认对整数/整数做int()