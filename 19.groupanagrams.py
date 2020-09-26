class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        dict = {}
        
        for word in strs:
            sortedWord = ''.join(sorted(word))
            
            if sortedWord in dict:
                dict[sortedWord].append(word)
                
            else:
                dict[sortedWord] = [word]

        for key,value in dict.items():
            res.append(value)
        return res