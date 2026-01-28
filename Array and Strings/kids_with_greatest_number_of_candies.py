class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        max_candy = max(candies)
        lol = []

        for i in range (len(candies)):
            if candies[i] + extraCandies >= max_candy:
                lol.append(True)
            else:
                lol.append(False)
        
        return lol

sol = Solution()
print(f' Test Case  1 : {sol.kidsWithCandies([4,2,1,1,2],1)}')

print(f' Test Case  1 : {sol.kidsWithCandies([12,1,12],10)}')

print(f' Test Case  1 : {sol.kidsWithCandies([2,3,5,1,3],3)}')


                       


        