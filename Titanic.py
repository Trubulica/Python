#importing libraries

import seaborn as sbrn
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#reading dataset

data = pd.read_csv("Titanic.csv")
data.head()

#change the columns’ names 

data.columns=["Name", "Survived", "Gender", "Age", "Class"]

#find the rows count

data.shape

#find the first 15 rows in our dataset

data.head(15)

#find the last 20 rows in our dataset 

data.tail(20)

#calculate the average age of passengers

data.Age.mean()

#find the oldest passenger’s age and name

data.max()
data[data["Age"].max() == data["Age"]] 

#find the total survivors’ count
data.groupby("Survived").count()

data_survived = data.groupby("Survived")
len(data_survived.get_group("yes"))

#find the youngest survivor age and name

survivor = data_survived.get_group("yes")
survivor[survivor["Age"].min() == survivor["Age"]]

#Find the 2nd Class passenger’s average age

classes = data.groupby("Class")
sec_class = classes.get_group("2nd")
sec_class["Age"].mean()

#Find the number of survivors of 3rd class passengers

classes = data.groupby(["Class", "Survived"])
len(classes.get_group(("3rd", "yes")))

#Find the average age of those who died from 1st class passengers

dead = data_survived.get_group("no")
dead_first = dead.groupby("Class")
dead_first.get_group("1st").mean()

#Create a pie chart that showed the distribution of passengers by class.

Labels = ["First Class","Second Class","Third Class"]
Sizes = len(classes.get_group("1st")),len(classes.get_group("2nd")),len(classes.get_group("3rd"))
Figure, Axes = plt.subplots()

Axes.pie(Sizes, labels=Labels,autopct = "%1.1f%%")
plt.show()

#Create a histogram that showed the distribution of passengers by age

Histogram = data.hist()
plt.show()

