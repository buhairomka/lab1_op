import random

matr=[[random.randint(0,10) for i in range(10)] for j in range(10)]
for i in matr:
	print(i)

nextmatr=[[0 for i in range(10)] for j in range(10)]
for i in range(len(matr)):
	for j in range(len(matr[0])):
		nextmatr[i][j]=matr[j][i]
for i in nextmatr:
	print(i)
		