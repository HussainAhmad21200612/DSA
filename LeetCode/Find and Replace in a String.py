class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        for index, source, target in sorted(zip(indices, sources, targets), reverse=True):
          if s[index:index + len(source)] == source:
            s = s[:index] + target + s[index + len(source):]
        return s
