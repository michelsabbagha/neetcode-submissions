class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d={}
        e={}
        if len(s) == len(t): #You wrote while len(s) == len(t):. Think about what while does: it repeats the body as long as the condition is true. But nothing inside your loop changes s or t, so if the lengths are equal, that condition stays true forever — infinite loop. It'll just hang.
            for i in range(len(s)):
                d[s[i]]=d.get(s[i],0)+1
                e[t[i]]=e.get(t[i],0)+1
            
            return e==d
            

        return False

