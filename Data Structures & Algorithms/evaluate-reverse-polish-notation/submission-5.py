class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        arr = []
        tmp = 0

        for i in range(len(tokens)):
            if tokens[i] == '+':
                tmp = arr[-2] + arr[-1]
                arr.pop()
                arr.pop()
                arr.append(tmp)

            elif tokens[i] == '-':
                tmp = arr[-2] - arr[-1]
                arr.pop()
                arr.pop()
                arr.append(tmp)

            elif tokens[i] == '*':
                tmp = arr[-2] * arr[-1]
                arr.pop()
                arr.pop()
                arr.append(tmp)

            elif tokens[i] == '/':
                tmp = int((arr[-2]) / arr[-1])
                arr.pop()
                arr.pop()
                arr.append(tmp)

            else:
                arr.append(int(tokens[i]))

        return arr[-1]