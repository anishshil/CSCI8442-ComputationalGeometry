import matplotlib.pyplot as plt

def plotClasses(c1, c2, pointPlot=True, scatterPlot=True):
    if pointPlot:
        plt.plot(c1[:,0],c1[:,1], 'k-', picker=5)
        plt.plot([c1[-1,0],c1[0,0]],[c1[-1,1],c1[0,1]], 'k-', picker=5)
        plt.plot(c2[:,0],c2[:,1], 'k-', picker=5)
        plt.plot([c2[-1,0],c2[0,0]],[c2[-1,1],c2[0,1]], 'k-', picker=5)
    if scatterPlot:
        plt.scatter(c1[:,0], c1[:,1])
        plt.scatter(c2[:,0], c2[:,1])
    plt.show()

def plot2D(data, hull, pause=False):
    plt.clf()
    plt.plot(hull[:,0],hull[:,1], 'b-', picker=5)
    plt.plot([hull[-1,0],hull[0,0]],[hull[-1,1],hull[0,1]], 'b-', picker=5)
    plt.plot(data[:,0],data[:,1],".r")
    # plt.axis('off')
    plt.show(block= not pause)
    if pause:
        plt.pause(0.0000001)

def plotLinesAndPointsInStep(L, P):
    plt.clf()		# Clear plt.fig
    plt.plot(L[:,0],L[:,1], 'b-', picker=5)	# Plot lines
    plt.plot(P[:,0],P[:,1],".r")		# Plot points
    plt.axis('off')		# No axis
    plt.show(block=False)	# Close plot
    plt.pause(0.0000001)	# Mini-pause before closing plot