class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        mapping={')':'(','}':'{',']':'[',}
        for bracket in s:
            if bracket in mapping:
                top=stack.pop() if len(stack)!=0 else '#'
                if top !=mapping[bracket]:
                    return False
            else:
                stack.append(bracket)

        return len(stack)==0

        