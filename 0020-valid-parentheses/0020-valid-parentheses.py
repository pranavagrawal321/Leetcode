class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        if len(s)%2 == 1:
            return False
        
        for i in s:
            if i in "([{":
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                else:
                    if (i == ")" and stack[-1] == "(") or (i == "}" and stack[-1] == "{") or (i == "]" and stack[-1] == "["):
                        stack.pop()
                    else:
                        return False
        
        return len(stack) == 0