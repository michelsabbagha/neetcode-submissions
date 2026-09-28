class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for word in strs:
            key = "".join(sorted(word)) #sorted-> list then join ->back to string but sorted 
            groups[key].append(word)

        return list(groups.values())


#Complexity — this one's new, pay attention: it's O(n · k log k), where n = number of words and k = the longest word's length. Why: you loop over n words (the n), and for each you sort it, and sorting a length-k word costs k log k. That's your first problem where the answer isn't plain O(n) — the log comes from the sorting step. Space is O(n·k) to store all the words in the groups.
        