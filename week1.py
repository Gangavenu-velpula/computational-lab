
#sum of two numbers

a=int(input('ENter a number:'))
b=int(input('ENter a number:'))
sum=a+b
print(sum)

#division of two numbers

a=5
b=1.5
c=type(a)
d=type(b)
if(c==int or c==float):
	if(d==int or d==float):
		div=a/b
		print(div)
else:
	print("invalid data type to find division value")
	print("Enter real number ")
	
	
#to find dot product of two vectors
	
a=[]
for i in range(1,3):
	x=int(input("enter: "))
	a.append(x)
	print(a)
b=[]
for i in range(1,3):
	y=int(input("enter: "))
	b.append(y)
	print(b)
dot_product=sum(x*y for x,y in zip(a,b))
print("dot_product",dot_product)

#to find determinant of matrix

def determinant(matrix):
	if len(matrix)!=2 or len(matrix[1])!=2:
		raise ValueError("Input matrix must be a 2*2 matrix")
	return matrix[0][0]*matrix[1][1]-matrix[0][1]
matrix_2=[[3,4],[3,4]]
result=determinant(matrix_2)
print("Determinant od 2*2 matrix",result)

