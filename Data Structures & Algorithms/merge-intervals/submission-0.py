class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda x: x[0]) 
        result = [intervals[0]]  
        for s, e in intervals[1:]: 
            last = result[-1]#bcz last is a reference to the last list of result then we can change last and it will change result automatically
            if s <= last[1]:
                last[1] = max(last[1], e)
            else:
                result.append([s, e]) 
        return result