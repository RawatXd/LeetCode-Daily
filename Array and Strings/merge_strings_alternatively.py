class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
            merged_str = []
            len1, len2 = len(word1), len(word2)
            min_len = min(len1, len2)
            for i in range(min_len):
                  merged_str.append(word1[i])
                  merged_str.append(word2[i])
            
            if len1>len2:
                  merged_str.append(word1[min_len:])
            else:
                  merged_str.append(word2[min_len:])
            
            return "".join(merged_str)
    