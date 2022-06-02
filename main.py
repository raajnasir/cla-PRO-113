import plotly.express as px
import pandas as pd

df = pd.read_csv("savings_data.csv")
fig = px.scatter(df, y = "quant_saved", color = "female")
fig.show()

import csv

with open('savings_data.csv', newline="") as f:
  reader = csv.reader(f)
  savings_data = list(reader)

savings_data.pop(0)

#Finding total number of people and number of people who were reminded
total_entries = len(savings_data)
total_people_given_reminder = 0
for data in savings_data:
  if int(data[3]) == 1:
    total_people_given_reminder += 1

import plotly.graph_objects as go

fig = go.Figure(go.Bar(x=["Reminded", "Not Reminded"], y=[total_people_given_reminder, (total_entries - total_people_given_reminder)]))

fig.show()


#Mean, median and mode of savings
import statistics
all_saving = []
for data in savings_data:
    all_saving.append(float(data[0]))
    
print(f"Mean of savings - {statistics.mean(all_saving)}") 
print(f"Median of savings - {statistics.median(all_saving)}") 
print(f"Mode of savings - {statistics.mode(all_saving)}") 

#Mean, median and mode of savings
remainded_savings = []
not_remainded_savings = []
for data in savings_data:
    if int(data[3]) == 1:
        remainded_savings.append(float(data[0]))
    else:
        not_remainded_savings.append(float(data[0]))

 

print("Results for people who were reminded to save") 
print(f"Mean of savings - {statistics.mean(remainded_savings)}") 
print(f"Median of savings - {statistics.median(remainded_savings)}") 
print(f"Mode of savings - {statistics.mode(remainded_savings)}") 
  #To add new lines
print("\n\n")
print("Results for people who were not reminded to save")
print(f"Mean of savings - {statistics.mean(not_remainded_savings)}") 
print(f"Median of savings - {statistics.median(not_remainded_savings)}") 
print(f"Mode of savings - {statistics.mode(not_remainded_savings)}") 

#To add new lines
print("\n\n")
print("Results for people who were not reminded to save")

std_deviation_all_savings = statistics.stdev(all_saving)
print("standard deviation of all savings : ", std_deviation_all_savings)

std_deviation_remainded = statistics.stdev(remainded_savings)
print("standars deviation of remainded savings : ", std_deviation_remainded)

std_deviation_not_remainded = statistics.stdev(not_remainded_savings)
print("standard deviation of not remainded savings : ", std_deviation_not_remainded)


import numpy as np
age = []
savings = []
for data in savings_data:
    if float(data[3]) != 0:
        age.append(float(data[2]))
        savings.append(float(data[0]))

correlation = np.corrcoef(age, savings) 
print(f"Correlation between the age of the person and their savings is - {correlation}")

import plotly.figure_factory as ff

fig = ff.create_distplot([df["quant_saved"].tolist()], ["Savings"], show_hist = False)
fig.show()

q1 = df["quant_saved"].quantile(0.25)
q3 = df["quant_saved"].quantile(0.75)
iqr = q3-q1
print(f"Q1 - {q1}")
print(f"Q2 - {q3}")
print(f"IQR - {iqr}")

lower_whisker = q1 - 1.5*iqr
upper_whisker = q3 + 1.5*iqr
print(f"Lower Whisker - {lower_whisker}")
print(f"Upper Whisker - {upper_whisker}")


