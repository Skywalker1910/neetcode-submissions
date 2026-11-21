class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching = {')':'(', ']':'[', '}':'{'}

        for char in s:
            if char in matching:
                if not stack:
                    return False
                
                top = stack.pop()

                if top != matching[char]:
                    return False

            else:
                stack.append(char)
        
        return len(stack) == 0