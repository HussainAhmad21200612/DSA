class Solution:
    def findAndReplace(self, s, Q, indexes, sources, targets):
        # code here 
        for index, source, target in sorted(zip(indexes, sources, targets), reverse=True):
          if s[index:index + len(source)] == source:
            s = s[:index] + target + s[index + len(source):]
        return s
