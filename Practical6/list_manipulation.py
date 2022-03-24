marks=[45, 36, 86, 57, 53, 92, 65, 45]
# List the mark he got in IBI classes
sorted(marks)
# returns sorted list, does not mutate marks
L = sorted(marks)
print(L)
# Print sorted marks
import matplotlib.pyplot as plt
# import graph drawing function
n = 8
# Sample amount equals to 8
plt.boxplot(marks,
            vert = True
            whis = 1.5
            patch_artist = True
            meanline = False
            showbox = True
            showcaps = True
            showfliers = True
            notch = False
              )
plt.show()
#Set boxplot parameters and run
c = sum(marks)/len(marks)
# Caculate the averge marks Rob got.  https://m.php.cn/article/472027.html
print("average is:", c)
if c >= 60:
print("Yes, Rob passed IBI")
else:
print("No, he failed")


