a = input("Father's age= ")
# Let users imput father's age
import re
#Import the regular expression module
b = re.findall(r"\d+\.?\d*",a)
# Take out the number in the sentence above
My_dict = ()
# Use dictionary command
risk = {'30':1.03, '35':1.07, '40':1.11, '45':1.17, '50':1.23, '55':1.32, '60':1.42, '65':1.55, '70':1.72,'75':1.94}
# Let farther age relate to offspring CHD risk
c = risk[b]
print(c)
# List the children CHD risk relateg to b
# I'm sorry, Professor. I want to design a more useful proggram, so I search for information from  https://blog.csdn.net/weixin_44178960/article/details/117266731
# However, The step " c = risk[b]" is not apply to dictionary  in Python, so I failed to run it.
# I try my best to finnish a more difficult project, but I failed. I'm sorry.