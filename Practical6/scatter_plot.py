L1 = [30, 35, 40, 45, 45, 50, 55, 60, 65, 70, 75]
# List father age
L2 = [1.03, 1.07, 1.11, 1.17, 1.23, 1.32, 1.42, 1.55, 1.72, 1.94]
# List children CHD risk
import matplotlib.pyplot as plt
# Import graph drawing function
N = 10
# Sample number equals to 10
x = L1
# Give x axis value
y = L2
# Give y axis value
plt.scatter(x, y, marker='o')
# Select blots as graph type