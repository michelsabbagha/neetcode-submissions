#class Solution:
    #def rob(self, nums: List[int]) -> int:
        #memo={} #dictionnary mapping the state to the answer for that state
        #def dfs(state):
            #if : #base case 
                #return 
            #if state in memo:
                #return memo[state]
            ##result=dfs(i)+dfs(i+2) #. The crucial property: the states you recurse into must be strictly closer to the base case, so the recursion keeps making progress toward stopping.
            #memo[state]=result
            #return result
        #return dfs()
#BASE CASE

        #The flow, in one mental picture: you call dfs(start) → it's not a base case and not cached, so it runs its recurrence, which calls dfs on smaller states → those cascade down until they hit base cases that return immediately → as each call finishes it stores its result and returns up. The first time a state is computed it lands in memo; if it's ever needed again elsewhere in the tree, line 6 returns it for free. That reuse is the entire speedup.


class Solution:
    def rob(self, nums: List[int]) -> int:
        memo={} 
        def dfs(i): #best money i can get from house i
            if i>len(nums)-1: 
                return 0
            if i in memo:
                return memo[i]
            result=max(nums[i]+dfs(i+2),dfs(i+1))
            memo[i]=result
            return result
        return dfs(0)    

