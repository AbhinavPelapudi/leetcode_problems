class Solution:
    def findReplaceString(self, S: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:
        if not S:
            return ""
        final_str = ""
        new_str = {}
        for i in range(len(indexes)):
            if indexes[i] + len(sources[i]) <= len(S) and sources[i] == S[indexes[i]: indexes[i] + len(sources[i])]:
                new_str[indexes[i]] = [targets[i], len(sources[i])]
        start = 0 
        while start < len(S):
            if start in new_str:
                final_str += new_str[start][0]
                start += new_str[start][1]
                continue
            final_str += S[start]
            start += 1
        return final_str