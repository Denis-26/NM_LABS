import numpy as np

def main():
	n = 4
	a = np.array([[4, 2, -1, 0.5], 
		 [1, -5, 2, 1  ],
		 [2, 1, -4, -1.5],
		 [1, -0.4, 0.8, -3]])
	a_free = np.array([30.5, -20, 6.5, 1.2] )

	b = np.zeros((n,n))
	c = np.eye(n)

	for i in range(n):
		b[i][0] = a[i][0]

	for j in range(n):
		c[0][j] = a[0][j]/b[0][0] 

	for i in range(1, n):
		for j in range(1, n):
			s = 0
			if i >= j:
				for k in range(j-1):
					s += b[i][k]*c[k][j]
				b[i][j] = a[i][j]-s
			if i < j:
				s = 0
				for k in range(i-1):
					s += b[i][k]*c[k][j]
				c[i][j] = 1/b[i][i]*(a[i][j]-s)
	print(b)
	print(c)

	print(np.dot(b,c))


if __name__ == "__main__":
	main()