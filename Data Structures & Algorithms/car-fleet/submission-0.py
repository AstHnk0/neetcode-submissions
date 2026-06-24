class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        stack = []
        for i in range(len(position)):
            cars.append([position[i], (target - position[i]) / speed[i]])
        cars.sort(reverse=True)
        for pos, time in cars:
            if not stack:
                stack.append(time)

            if time > stack[-1]:
                stack.append(time)

            if time <= stack[-1]:
                continue
            
        return len(stack)



            