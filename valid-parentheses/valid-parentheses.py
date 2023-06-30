class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
    
        stack = []
        for i in s:
            if i in "([{":
                stack.append(i)
            elif i in ")]}":
                if len(stack) == 0:
                    return False
                if i == ")" and stack[-1] == "(":
                    stack.pop()
                elif i == "}" and stack[-1] == "{":
                    stack.pop()
                elif i == "]" and stack[-1] == "[":
                    stack.pop()
                else:
                    return False
        return len(stack) == 0