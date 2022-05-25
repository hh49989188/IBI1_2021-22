import os
import pandas as pd
# utilize pandas as library
os.chdir("D:/cygwin/IBI1_2021-22/Practical7")
covid_data = pd.read_csv("full_data.csv")
# use the pandas library to read the content of the.csv ﬁle into a data frame object
covid_data.iloc[10:21,[0,2]]
print(covid_data.iloc[10:21,[0,2]])
# show the ﬁrst and third columns from rows 10-20(inclusive)
my_rows = list(covid_data.loc[:, "location"])
# list the location column
Afghanistan = []
# Creat a list called Afghanistan
for i in range(0, len(my_rows)):
  Afghanistan. append(my_rows[i] == "Afghanistan")
# It means that if my_rows[i] is True, it will be added into list
# If my_rows[i] is False(do not equal to Afghanistan), the list will not expend
if my_rows[i] == "Afghanistan":
    a = True
else:
    a = False
print(covid_data.loc[Afghanistan, "total_cases"])

China_data = []
for i in range(0, len(my_rows)):
    China_data. append(my_rows[i] == "China")
print(covid_data.loc[China_data, ])
# Use China_data to store figure about China in a list, same principle as Afghanistan above

import numpy as np
mean = np.mean(covid_data.loc[China_data, ["new_cases", "new_deaths"]])
# Use numpy to compute the mean of new cases and new deaths in China
print(mean)
# new cases mean = 893.923913, new deaths mean = 35.967391

import matplotlib.pyplot as plt
x = covid_data.loc[China_data, ["new_cases", "new_deaths"]]
plt.boxplot(x, vert=True, whis=1.5, labels=["new cases", "new deaths"], showbox=True)
# Sets the parameters of the boxplot
plt.title("boxplots of new cases and new deaths in China")
plt.show()

china_dates = covid_data.loc[China_data, "date"]
china_new_cases = covid_data.loc[China_data, "new_cases"]
china_new_deaths = covid_data.loc[China_data, "new_deaths"]
# Identify 3 variables to makes plot
plt.plot(china_dates, china_new_cases, 'b+', label="new cases")
plt.plot(china_dates, china_new_deaths, 'r+', label="new deaths")
# Adjust some parameters in plots
plt.legend()
plt.title("China new cases and deaths")
plt.xticks(china_dates.iloc[0:len(china_dates):4], rotation=-90)
plt.ylabel("cases/deaths number")
# Set the parameters of the plots
plt.legend()
plt.show()

# Question:How have new cases and total cases developed overtime in Spain?
Spain_data = []
for i in range(0, len(my_rows)):
    Spain_data. append(my_rows[i] == "Spain")
print(covid_data.loc[Spain_data, ])
# Use Spain_data to store figure about Spain in a list, same principle as Afghanistan above

Spain_dates = covid_data.loc[Spain_data, "date"]
Spain_new_cases = covid_data.loc[Spain_data, "new_cases"]
Spain_total_cases = covid_data.loc[Spain_data, "total_cases"]
# Identify 3 variables to makes plot
plt.plot(Spain_dates, Spain_new_cases, 'b+', label="new cases")
plt.plot(Spain_dates, Spain_total_cases, 'r+', label="total cases")
# Adjust some parameters in plots
plt.legend()
plt.title("Spain new cases and total cases change over time")
plt.xticks(Spain_dates.iloc[0:len(Spain_dates):4], rotation=-90)
plt.ylabel("new/total cases number")
# Set the parameters of the plots
plt.legend()
plt.show()
# Discussion part are in question.txt
