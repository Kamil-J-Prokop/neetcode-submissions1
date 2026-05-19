class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_stack = []

        times_of_arrival = []

        for car in range(len(position)):
            toa = (target - position[car]) / speed[car]
            times_of_arrival.append((position[car], toa))

        times_of_arrival.sort(reverse=True)

        for car in range(len(times_of_arrival)):
            if not pos_stack:
                pos_stack.append(times_of_arrival[car][1])
            
            elif times_of_arrival[car][1] > pos_stack[-1]:
                pos_stack.append(times_of_arrival[car][1])

        return len(pos_stack)
        