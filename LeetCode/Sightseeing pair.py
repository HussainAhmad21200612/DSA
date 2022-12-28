class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        maxx=0
        aplusi=values[0]+0

        for i in range(1,len(values)):
            maxx=max(maxx,aplusi+values[i]-i)
            aplusi=max(aplusi,values[i]+i)
            
        return maxx
