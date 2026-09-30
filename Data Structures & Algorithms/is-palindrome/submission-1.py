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

#easier
#cleaned = [c.lower() for c in s if c.isalnum()]
#return cleaned == cleaned[::-1]
#cleaned[::-1] is Python's slice syntax for reversing a list (or string). Let me break it down.

#Slicing has three parts: sequence[start : stop : step]

#start — where to begin (default: the beginning)
#stop — where to end, exclusive (default: the end)
#step — how to move through it (default: 1, i.e. one #forward at a time)

#In [::-1], start and stop are both left blank, and step is -1:

#step = -1 means "go backwards, one element at a time."
#With a negative step, the blank start/stop flip to mean "from the end to the beginning."

#So [::-1] reads as: "take the whole thing, stepping backwards" → the reversed sequence.
        