n=0
# The number of cutting pizza from 1 to infinity
p=0
while p < 64:
     n=n+1
     p=(n ** 2+n+2)/2
# The equation tells the relationship between n and p
     print("Hello, professor.The cutting number is")
     print(n)
     print("The slice number is")
     print(p) 
