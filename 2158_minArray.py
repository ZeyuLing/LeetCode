class Solution(object):
    def minArray(self, numbers):
        """
        :type numbers: List[int]
        :rtype: int
        """
        #[3,4,5,6,7,7,1,2]
        left=0
        right=len(numbers)-1
        while(left<right):
            pivot=int((left+right)/2)
            if(numbers[right]>numbers[pivot]):
                #如果右边比中间大 则pivot到right的部分一定顺序，间断点在pivot及其左侧
                right=pivot
            elif (numbers[right]<numbers[pivot]):   #如果右侧比中间小，间断点一定在pivot到right之间
                left=pivot+1
            else:   #中=右，则无法判断，但可以排除1个。
                right-=1

        return numbers[left]