class Solution(object):
    def countBits(self, num):
        bitCount = [0, 1]
	p = 0
	while True:
	    if num / 2**p <= 1: break
	        p += 1
	
	for i in range(p):
	    bitCount = bitCount + [c+1 for c in bitCount]
								            
	return bitCount[:num+1]
