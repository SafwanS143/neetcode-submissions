class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minSpeed = 1
        maxSpeed = max(piles)

        while minSpeed < maxSpeed:
            midSpeed = (maxSpeed + minSpeed) // 2
            midTime = 0

            print("speed:", midSpeed)

            for pile in piles:
                midTime += - (pile // - midSpeed)

            print("Time:", midTime)

            if midTime <= h:
                maxSpeed = midSpeed

            else:
                minSpeed = midSpeed + 1
        
        return minSpeed