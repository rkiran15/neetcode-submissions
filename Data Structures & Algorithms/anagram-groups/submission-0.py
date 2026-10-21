class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapping = {}
        for word in strs:
            sort_word = ''.join(sorted(word))
            if mapping.get(sort_word,'') == '':
                mapping[sort_word] = [word]
            else:
                mapping[sort_word].append(word)
        return list(mapping.values())