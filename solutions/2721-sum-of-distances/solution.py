class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        d=defaultdict(list)
        for i,num in enumerate(nums):
            d[num].append(i)
        a=[0]*len(nums)
        for values in d.values():
            if len(values)>1:
                c=len(values)
                idx=values[0]
                a[idx]=sum(values)-c*idx
                i,j=0,c-2
                for n in values[1:]:
                    a[n]=a[idx]+(i-j)*(n-idx)
                    i+=1
                    j-=1
                    idx=n
        return a
