class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        d = {}
        for i in range(len(strs)):
            dummystring = "".join(sorted(strs[i]))
            if dummystring not in d:
                d[dummystring] = []
            d[dummystring].append(strs[i])
        
        return list(d.values())

            