class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        corners=set()
        c=lambda k:k[0]+k[1]
        a = lambda: (Y-y) * (X-x)
        area=0
        for x, y, X, Y in rectangles:
            area += a()
            corners ^= {(x, Y), (X, y), (x, y), (X, Y)}
    
        if len(corners) != 4:
            return False
        x, y = min(corners, key = c)
        X, Y = max(corners, key = c)
        return area == a()
