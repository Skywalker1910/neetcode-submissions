class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for word in strs:
            key = "".join(sorted(word))
            if key in groups:
                groups[key].append(word)
                continue
            
            groups[key].append(word)
        
        return list(groups.values())