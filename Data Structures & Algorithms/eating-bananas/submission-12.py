class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minSpeed = 1
        maxSpeed = max(piles)

        while minSpeed < maxSpeed:
            midSpeed = (maxSpeed + minSpeed) // 2
            midTime = 0

            for pile in piles:
                midTime += - (pile // - midSpeed)

            if midTime <= h:
                maxSpeed = midSpeed

            else:
                minSpeed = midSpeed + 1
        
        return minSpeed