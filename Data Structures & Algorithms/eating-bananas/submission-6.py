class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        search_space_bot = 1
        search_space_top = max(piles)

        answer = search_space_top

        def can_finish(k: int) -> bool:
            hours = 0

            for pile in piles:
                hours += -(pile // -k)
                if hours > h:
                    return False
            
            return True


        while search_space_bot <= search_space_top:
            mid = search_space_bot + (search_space_top - search_space_bot)//2

            if can_finish(mid):
                answer = mid
                search_space_top = mid - 1
            else:
                search_space_bot = mid + 1
        
        return answer
        
        """
        from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_finish_at_speed(k: int) -> bool:
            hours = 0

            for pile in piles:
                hours += (pile + k - 1) // k

                if hours > h:
                    return False

            return True

        left = 1
        right = max(piles)
        answer = right

        while left <= right:
            mid = left + (right - left) // 2

            if can_finish_at_speed(mid):
                answer = mid
                right = mid - 1
            else:
                left = mid + 1

        return answer

           

        """
