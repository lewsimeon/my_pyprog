class solution:
    def search(self, nums, target):
        left=0
        right=len(nums)-1
        ans=-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                ans=mid
                right=mid-1
            elif nums[mid]<target:
                left=mid+1
            elif nums[mid]>target:
                right=mid-1
        return ans

nums=[1,2,3,4,5,6,7,8,9]
target=4
print(solution().search(nums,target))
