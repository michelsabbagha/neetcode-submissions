class Solution:
    def isPalindrome(self, s: str) -> bool:
        left=[]
        right=[]
        for i in range(len(s)):
            if s[i].isalnum():
                #s[i].lower()-->Bug 1 — s[i].lower() does nothing. Strings are immutable, so .lower() doesn't change s[i] in place — it returns a new lowercased string, which you're throwing away. Then you append the original s[i] (still uppercase). You have to capture the return value: append the lowercased char directly.
                left.append(s[i].lower())
        for j in range(len(s)-1,-1,-1):
            if s[j].isalnum():
                right.append(s[j].lower())
        return left==right

        