class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)
        
        for word in strs:
            anagrams[''.join(sorted(word))].append(word)
            # 문자열 정렬 : sorted(str)
            # sorted(str) -> [s, t, r] 형태로 정렬되므로 ''.join(sorted(str))로 다시 합쳐주자!
            
        return list(anagrams.values())
        