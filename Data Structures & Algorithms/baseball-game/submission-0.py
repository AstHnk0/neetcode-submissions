class Solution:
    def calPoints(self, operations: List[str]) -> int:
        total_sum = 0
        stack = []
        for i in range(len(operations)):
            if operations[i] == '+':
                stack.append(stack[-1] + stack[-2])

            elif operations[i] == 'D':
                stack.append(stack[-1] * 2)

            elif operations[i] == 'C':
                stack.pop()

            else:
                stack.append(int(operations[i]))
        total_sum = sum(stack)
        return total_sum