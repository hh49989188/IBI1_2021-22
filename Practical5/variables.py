a=19245301
# a is a total cases of COVID-19 in the UK till 2022
b=4218520
# b is a total cases of COVID-19 in the UK till 2021
c=271
# c is a total cases of COVID-19 in the UK till 2020
d=b-c
# d is a difference between total cases of COVID-19 in the UK 2021&2020
e=a-b
# e is a difference between total cases of COVID-19 in the UK 2021&2022
print ("Hello, professor.The difference between 2021 and 2020 is")
print (d)
print ("The difference between 2021 and 2022 is")
print (e)
e>d
# compare e and d
print ("e is larger")
r1=(b-c)/c
# caculate increasing rate in 2020-21
r2=(a-b)/b
# caculate increasing rate in 2021-22
print ("The rate in 2020-2021 is")
print (r1)
print ("The rate in 2021-2022 is")
print (r2)
if r1>r2:
        print ("The rate in 2020-21 is larger")
else:
        print ("The rate in 2021-22 is larger")
# compare r1 and r2

# Boolean variable
X="hello"
Y="world"
W=X and Y
print(W)
w=X or Y
print(w)
