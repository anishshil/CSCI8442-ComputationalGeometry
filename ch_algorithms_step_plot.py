import numpy as np
import matplotlib.pyplot as plt
from visualization import *

# Function to know if we have a CCW turn
def CCW(p1, p2, p3):
	if (p3[1]-p1[1])*(p2[0]-p1[0]) >= (p2[1]-p1[1])*(p3[0]-p1[0]):
		return True
	return False

# GRAHAM SCAN
def GrahamScanAnimation(P, pauseDuration=0.0000001):
	P.sort()			# Sort the set of points
	P = np.array(P)			# Convert the list to numpy array
	plt.figure()			# Create a new fig
	L_upper = [P[0], P[1]]		# Initialize the upper part
	# Compute the upper part of the hull
	for i in range(2,len(P)):
		L_upper.append(P[i])
		while len(L_upper) > 2 and not CCW(L_upper[-1],L_upper[-2],L_upper[-3]):
			del L_upper[-2]
		L = np.array(L_upper)
		plotLinesAndPointsInStep(L, P, pauseDuration)
	L_lower = [P[-1], P[-2]]	# Initialize the lower part
	# Compute the lower part of the hull
	for i in range(len(P)-3,-1,-1):
		L_lower.append(P[i])
		while len(L_lower) > 2 and not CCW(L_lower[-1],L_lower[-2],L_lower[-3]):
			del L_lower[-2]
		L = np.array(L_upper + L_lower)
		plotLinesAndPointsInStep(L, P, pauseDuration)
	del L_lower[0]
	del L_lower[-1]
	L = L_upper + L_lower 		# Build the full hull
	plt.axis('off')
	plt.show()
	return np.array(L)

# JARVIS' MARCH
def JarvisMarchAnimation(S, pauseDuration=0.0000001):
	plt.figure()  # Define figure
	index = 0
	n = len(S)
	P = [None] * n
	l = np.where(S[:,0] == np.min(S[:,0]))
	pointOnHull = S[l[0][0]]
	i = 0
	while True:
		P[i] = pointOnHull
		endpoint = S[0]
		for j in range(1,n):
			if (endpoint[0] == pointOnHull[0] and endpoint[1] == pointOnHull[1]) or not CCW(S[j],P[i],endpoint):
				endpoint = S[j]
		i = i + 1
		pointOnHull = endpoint
		J = np.array([P[k] for k in range(n) if P[k] is not None])
		plotLinesAndPointsInStep(J, S, pauseDuration)
		index += 1
		if endpoint[0] == P[0][0] and endpoint[1] == P[0][1]:
			break
	for i in range(n):
		if P[-1] is None:
			del P[-1]
	P = np.array(P)
	plot2D(S, P, pause=True)
	return P