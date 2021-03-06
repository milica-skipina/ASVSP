import os

from tabulate import tabulate
import pandas as pd
import matplotlib.pyplot as plt


id = input("ID pacijenta:")
year = input("Godina:")
month = input("Mjesec:")
day = input("Dan:")

if year == "*" and month == "*" and day == "*":
    file = "../results/statistics_percentage.csv"
    df = pd.read_csv(file,  sep=',', engine='python')
    df.columns = ['PtID', 'VeryHigh', 'High', 'InRange', 'Low', 'VeryLow']
    df = df.loc[df['PtID'] == int(id)]
else:
    file = "../results/statistics.csv"
    df = pd.read_csv(file,  sep='|', engine='python')
    df.columns = ['PtID', 'Year', 'Month', 'Day', 'VeryHigh', 'High', 'InRange', 'Low', 'VeryLow']
    df = df.loc[df['PtID'] == int(id)]
    if year != '*':
        df = df.loc[df['Year'] == int(year)] 
    if month != '*':
        df = df.loc[df['Month'] == int(month)] 
    if day != '*':
        df = df.loc[df['Day'] == int(day)] 

if df.size > 0:
    print(tabulate(df, headers = 'keys', tablefmt = 'psql'))
    df = df.groupby(['PtID']).agg({'VeryHigh':'sum','High':'sum', 'InRange':'sum', 'Low':'sum', 'VeryLow':'sum'})
    # Data to plot
    labels = 'Very High', 'High', 'In Range', 'Low', 'Very Low'
    sizes = [df.VeryHigh.values[0], df.High.values[0], df.InRange.values[0], df.Low.values[0], df.VeryLow.values[0]]
    colors = ['red', 'orange', 'green', 'lightskyblue', 'blue']

    # Plot
    patches, texts = plt.pie(sizes, colors=colors, shadow=True, startangle=90)
    plt.legend(patches, labels, loc="best")
    plt.axis('equal')
    plt.tight_layout()
    plt.show()
else:
    print("Ne postoje podaci za unesene parametre.")

# Otkomentarisati za prikaz boxplot-a 

# gender_file = "../results/gender_glucose.csv"
# df_gender = pd.read_csv(gender_file,  sep=',', engine='python')

# female = df_gender.loc[df_gender["Gender"] == 'F']
# male = df_gender.loc[df_gender["Gender"] == 'M']

# # print(tabulate(female, headers = 'keys', tablefmt = 'psql'))
# # print(tabulate(male, headers = 'keys', tablefmt = 'psql'))

# female_data = female.GlucoseValue
# male_data = male.GlucoseValue

# data = [female_data, male_data]
# fig = plt.figure(figsize =(10, 7))
# ax=fig.add_subplot(111)
# # ax.set_yticklabels(['0', '25', '50', '75', '100', '125', '150', '175', '200', '225', '250'])
# ax.set_xticklabels(['Female', 'Male'])
# bp = ax.boxplot(data)
# plt.show()
