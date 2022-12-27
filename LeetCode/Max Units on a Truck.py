class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        ll=[]
        def maxx(r):
            return r[1]
        boxTypes.sort(key=maxx,reverse=True)
        i=0
        j=0
        while(j<len(boxTypes)):
            if truckSize==0:
                break
            if boxTypes[j][0]<=truckSize:
                    i+=boxTypes[j][1]*boxTypes[j][0]
                    truckSize-=boxTypes[j][0]
            else:
                i+=abs(truckSize)*boxTypes[j][1]
                break
            j+=1
        return i
