class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length=len(nums)
        i=0
        while(i<length and nums[i]!=0):
            i=i+1
        def move(start,end,nums):
            a=start
            while(a<length and nums[a]==0):
                a=a+1
            b=a
            while(b<length and nums[b]!=0):
                b=b+1
            next=start+(b-a)
            nums[start:next]=nums[a:b]
            nums[next:b]=[0]*(b-next)
            if b==length:
                pass
            else:
                move(next,end,nums)
        move(i,length,nums)
º¯ÊýÊ½Î²µÝ¹é
length=len(nums)
        def move(start,count):
            if start>=length:
                pass
            else:
                if nums[start]==0:
                    move(start+1,count+1)
                else:
                    if count!=0:
                        nums[start-count]=nums[start]
                        nums[start]=0
                    move(start+1,count)
        move(0,0)