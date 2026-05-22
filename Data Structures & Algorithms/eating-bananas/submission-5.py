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
        k = 1

        while k <= max(piles):
            total_time = 0
            for i in piles:
                time_pile = -(i // -k)
                #print(f"i: {i}, k: {k}, Time pile: {time_pile}")
                total_time += time_pile
            #print(f"Total time: {total_time}")
            if total_time <= h:
                return k

            k += 1

        """
