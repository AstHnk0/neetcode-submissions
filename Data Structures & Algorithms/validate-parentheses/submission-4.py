class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(s[i])
            if s[i] == ')':
                if len(stack) > 0 and stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            
            if s[i] == '{':
                stack.append(s[i])
            if s[i] == '}':
                if len(stack) > 0 and stack[-1] == '{':
                    stack.pop()
                else:
                    return False

            if s[i] == '[':
                stack.append(s[i])
            if s[i] == ']':
                if len(stack) > 0 and stack[-1] == '[':
                    stack.pop()
                else: return False


        if len(stack) > 0:
            return False
        else:
            return True