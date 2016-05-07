class Solution(object):
    def maxPoints(self, points):
	"""
	:type points: List[Point]
	:rtype: int
	"""
	if len(points) <= 2: return len(points)
	ans = 0
	for i, p1 in enumerate(points):
	    slope = {}
	    dup = 0
	    for p2 in points[i+1:]:
	        if p2 == p1: continue
		else:
		    if p2.x == p1.x:
			if p2.y == p1.y:
			    dup += 1
			    continue
			s = 'inf'
		    else: 
		        s = float(p2.y - p1.y) / (p2.x - p1.x)
		        if s not in slope:
		            slope[s] = 2
		        else:
		            slope[s] += 1
	    if slope:
	        ans = max(ans, max(slope.values())+dup)
	    else:
	        ans = max(ans, dup + 1)
	return ans
