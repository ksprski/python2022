import sys
x = float(sys.argv[1])
if (x > 0): 
	print('sgn('+str(sys.argv[1])+') = 1')
elif (x == 0):
 	print('sgn('+str(sys.argv[1])+') = 0')
else:	
	print('sgn('+str(sys.argv[1])+') = -1')