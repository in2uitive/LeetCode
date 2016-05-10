class Solution(object):
    def isValidSerialization(self, preorder):
        preorder = preorder.split(',')
	if preorder == ['#']: return True
	if len(preorder) < 3: return False
	if preorder[0] == '#': return False
	stack = []
	for n in preorder:
	    #print n, stack
	    if n == '#':
	       if stack[-1] == '#':
	           while len(stack) > 1 and stack[-1] == '#':
		       #print '\t', stack
		       stack.pop()
		       stack.pop()
	    stack.append(n)

	#print stack
	if stack != ['#']:
	    return False
	return True
