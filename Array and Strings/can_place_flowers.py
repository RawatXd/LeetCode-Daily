class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        # If no flowers need to be planted, we're already done!
        if n == 0:
            return True
            
        for i in range(len(flowerbed)):
            # Check if the current plot is empty
            if flowerbed[i] == 0:
                # Check if the left plot is empty (or it's the start of the bed)
                prev_empty = (i == 0) or (flowerbed[i - 1] == 0)
                # Check if the right plot is empty (or it's the end of the bed)
                next_empty = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)
                
                if prev_empty and next_empty:
                    # Plant a flower here!
                    flowerbed[i] = 1
                    n -= 1
                    
                # If we've planted all required flowers, return True early
                if n <= 0:
                    return True
        
        return n <= 0

# Testing the logic
sol = Solution()
print(f'Case 1 : {sol.canPlaceFlowers([1,0,0,0,1], 1)}') # Expected: True
print(f'Case 2 : {sol.canPlaceFlowers([1,0,0,0,1], 2)}') # Expected: False