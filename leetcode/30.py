from typing import List
from collections import Counter
class Solution:

    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not  words:
            return []
        num = len(words[0])
        total_num = len(words) * num

        mapping = Counter(words)
        res = []
        # print(mapping_copy)
        for i in range(len(s) - total_num + 1):
            test = []
            for j in range(i,i+total_num , num):
                test_string = s[j:j+num]
                if test_string in mapping.keys() and mapping.get(test_string) >0 :
                    mapping[test_string] -=1
                    test.append(0)
                    if test == ([0] * len(words)):
                        res.append(i)
                        mapping = Counter(words)
                else:
                    continue
            mapping = Counter(words)
            
            continue
        return res


print(Solution().findSubstring("abaababbaba",["ab","ba","ab","ba"]))