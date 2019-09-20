import numpy as np
import matplotlib.pyplot as plt

class K_Mean_Algorithm:
	def __init__(self, k, epochs):
		self.k = k
		self.epochs = epochs
	def train(self, S_x, S_y):
		# To define clusters, need to know the range
		max_X, min_X = np.max(S_x), np.min(S_x)
		max_Y, min_Y = np.max(S_y), np.min(S_y)
		# Clusters
		self.C_x = np.random.uniform(min_X,max_X, size=(self.k,1))
		self.C_y = np.random.uniform(min_Y,max_Y, size=(self.k,1))

		for m in range(1,self.epochs):
			plt.figure()
			plt.scatter(C_x, C_y, c = 'black')
			# Error in obtaining Voronoi Cells
			errors = np.zeros((self.k,1))
			# Voronoi Cells
			VoronoiCell = np.zeros((self.k,len(S_x),2))
			abs_V = np.zeros((self.k,1))
			for i in range(len(S_x)):
				for j in range(self.k):
					errors[j] = np.square(self.C_x[j] - S_x[i]) + np.square(self.C_y[j] - S_y[i])
				ind = np.argmin(errors)
				VoronoiCell[ind, i, :] = [S_x[i], S_y[i]]

			# Calculating the new cluster centers
			for i in range(self.k):
				abs_V[i] = len(np.nonzero(VoronoiCell[i,:,0])[0])
				if not abs_V[i] == 0:
					self.C_x[i] = sum(VoronoiCell[i,:,0]) / abs_V[i]
					self.C_y[i] = sum(VoronoiCell[i,:,1]) / abs_V[i]
			prop_cycle = plt.rcParams['axes.prop_cycle']
			colors = prop_cycle.by_key()['color']
			for i in range(self.k):
				plt.scatter(VoronoiCell[i,:,0],VoronoiCell[i,:,1], c = colors[i])
			plt.legend(['Clusters'])
			plt.show()
	def predict(self,point):
		X, Y = point[0], point[1]
		error = np.zeros((self.k,1))
		for i in range(self.k):
			error[i] = np.square(self.C_x[j] - X) + np.square(self.C_y[j] - Y)
		ind = np.argmin(error)
		return [self.C_x[ind], self.C_y[ind]]
