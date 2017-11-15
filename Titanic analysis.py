#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat May 27 18:30:16 2017

@author: jie
"""
# data analysis and wrangling
import pandas as pd
import numpy as np
import random as rnd

# visualization
import seaborn as sns
import matplotlib.pyplot as plt
#matplotlib inline

# machine learning
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC, LinearSVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import Perceptron
from sklearn.linear_model import SGDClassifier
from sklearn.tree import DecisionTreeClassifier


train_df = pd.read_csv("/Users/jie/Documents/kaggle/Titanic/train.csv")
test_df = pd.read_csv("/Users/jie/Documents/kaggle/Titanic/test.csv")
combine = [train_df, test_df]

#########################################
###########Data description##############
'''
print(train_df.columns.values)
print(train_df.head())
print(train_df.tail())


train_df.info() #===>>>AGE, CABIN AND EMBARKED are missing
print(train_df["Age"].describe(percentiles=[.1, .2, .3, .4, .5, .6, .7, .8, .9, .99]))
print(train_df.describe(include=['O']))
'''


###################################################
###########Analysis by pivot features##############
pclass_table=train_df[['Pclass', 'Survived']].groupby(['Pclass'], 
                      as_index=False).mean().sort_values(by='Survived', ascending=False)
#print(pclass_table)


###################################################
###########Check Correlations######################
'''
#one numerical data VS outcome (survival)
g = sns.FacetGrid(train_df, col='Survived')
g.map(plt.hist, 'Fare', bins=40)

#one categorical data VS outcome (survival) -- Frequency Table
pclass_table=train_df[['Embarked', 'Survived']].groupby(['Embarked'], 
                      as_index=False).mean().sort_values(by='Survived', ascending=False)
print(pclass_table)
               

##Or
grid = sns.FacetGrid(train_df, size=2.2, aspect=1.6)
grid.map(sns.pointplot, 'Pclass', 'Survived', palette='deep')
grid.add_legend()


#One continuous, one categorical vs out
grid = sns.FacetGrid(train_df, col='Survived', row='Embarked', size=2.2, aspect=1.6)
grid.map(plt.hist, 'Age', alpha=.7, bins=20) ##alpha control colors
grid.add_legend();
               
#Two categorical vs out
grid = sns.FacetGrid(train_df, size=2.2, aspect=1.6)
grid.map(sns.pointplot, 'Sex', 'Survived', 'Embarked',palette='deep')
grid.add_legend()


#One Continuous, 2 cate ===>>>>Not possible


#2+Cates               
grid = sns.FacetGrid(train_df, row='Sex', size=2.2, aspect=1.6)
grid.map(sns.pointplot, 'Pclass', 'Survived', 'Embarked', palette='deep')
grid.add_legend()
'''

###################################################
###########Explore other features##################
for dataset in combine:
    dataset['Title'] = dataset.Name.str.extract(' ([A-Za-z]+)\.', expand=False)


pclass_table=train_df[['Title', 'Survived']].groupby(['Title'], 
                      as_index=False).mean().sort_values(by='Survived', ascending=False)

#Clerify the rare title
for dataset in combine:
    dataset['Title'] = dataset['Title'].replace(['Lady', 'Countess','Capt', 'Col',\
 	'Don', 'Dr', 'Major', 'Rev', 'Sir', 'Jonkheer', 'Dona'], 'Rare')

    dataset['Title'] = dataset['Title'].replace('Mlle', 'Miss')
    dataset['Title'] = dataset['Title'].replace('Ms', 'Miss')
    dataset['Title'] = dataset['Title'].replace('Mme', 'Mrs')
    
train_df[['Title', 'Survived']].groupby(['Title'], as_index=False).mean()



###################################################
###########Categorical Conversion##################
title_mapping = {"Mr": 1, "Miss": 2, "Mrs": 3, "Master": 4, "Rare": 5}
for dataset in combine:
    dataset['Title'] = dataset['Title'].map(title_mapping).astype(int)
    dataset['Title'] = dataset['Title'].fillna(0).astype(int)


for dataset in combine:
    dataset['Sex'] = dataset['Sex'].map( {'female': 1, 'male': 0} ).astype(int)


###################################################
###########Completing Data#########################
###Continuous
#Generate missing age based on Pclass and Sex (most correlated)
guess_ages = np.zeros((2,3)) #2 sex *3pclass
guess_ages

for dataset in combine:
    for i in range(0, 2):
        for j in range(0, 3):
            guess_df = dataset[(dataset['Sex'] == i) & \
                                  (dataset['Pclass'] == j+1)]['Age'].dropna()

            age_mean = guess_df.mean()
            age_std = guess_df.std()
            age_guess = rnd.uniform(age_mean - age_std, age_mean + age_std)


            # Convert random age float to nearest .5 age
            guess_ages[i,j] = int( age_guess/0.5 + 0.5 ) * 0.5
            
    for i in range(0, 2):
        for j in range(0, 3):
            dataset.loc[ (dataset.Age.isnull()) & (dataset.Sex == i) & (dataset.Pclass == j+1),\
                    'Age'] = guess_ages[i,j]

    dataset['Age'] = dataset['Age'].astype(int)

train_df.head()

#create age bands
train_df['AgeBand'] = pd.cut(train_df['Age'], 5)
train_df[['AgeBand', 'Survived']].groupby(['AgeBand'], as_index=False).mean().sort_values(by='AgeBand', ascending=True)

for dataset in combine:    
    dataset.loc[ dataset['Age'] <= 16, 'Age'] = 0
    dataset.loc[(dataset['Age'] > 16) & (dataset['Age'] <= 32), 'Age'] = 1
    dataset.loc[(dataset['Age'] > 32) & (dataset['Age'] <= 48), 'Age'] = 2
    dataset.loc[(dataset['Age'] > 48) & (dataset['Age'] <= 64), 'Age'] = 3
    dataset.loc[ dataset['Age'] > 64, 'Age']
train_df.head()

train_df['AgeBand'].describe()
train_df['AgeBand'].value_counts()


#create fare bond
test_df['Fare'].fillna(test_df['Fare'].dropna().median(), inplace=True)

for dataset in combine:
    dataset.loc[ dataset['Fare'] <= 7.91, 'Fare'] = 0
    dataset.loc[(dataset['Fare'] > 7.91) & (dataset['Fare'] <= 14.454), 'Fare'] = 1
    dataset.loc[(dataset['Fare'] > 14.454) & (dataset['Fare'] <= 31), 'Fare']   = 2
    dataset.loc[ dataset['Fare'] > 31, 'Fare'] = 3
    dataset['Fare'] = dataset['Fare'].astype(int)


###Categorical
freq_port = train_df.Embarked.dropna().mode()[0] #get the mode of Embarked values, and take the first one

for dataset in combine:
    dataset['Embarked'] = dataset['Embarked'].fillna(freq_port)

for dataset in combine:
    dataset['Embarked'] = dataset['Embarked'].map( {'S': 0, 'C': 1, 'Q': 2} ).astype(int)

###################################################
###########Combine info############################
for dataset in combine:
    dataset['FamilySize'] = dataset['SibSp'] + dataset['Parch'] + 1

train_df[['FamilySize', 'Survived']].groupby(['FamilySize'], as_index=False).mean().sort_values(by='Survived', ascending=False)



for dataset in combine:
    dataset['IsAlone'] = 0
    dataset.loc[dataset['FamilySize'] == 1, 'IsAlone'] = 1

train_df[['IsAlone', 'Survived']].groupby(['IsAlone'], as_index=False).mean()



#################################################
###############Drop useless data#################


train_df = train_df.drop(['PassengerId','Parch','Name','SibSp','Ticket','Cabin','AgeBand'], axis=1)

combine = [train_df, test_df]

X_train = train_df.drop("Survived", axis=1)
Y_train = train_df["Survived"]



#################################################
###############Model Comperasion#################


# Logistic Regression

logreg = LogisticRegression()
logreg.fit(X_train, Y_train)
acc_log = round(logreg.score(X_train, Y_train) * 100, 2) #Returns the mean accuracy on the given train data and labels
print acc_log

coeff_df = pd.DataFrame(train_df.columns.delete(0)) #delete first col == outcome
coeff_df.columns = ['Feature']
coeff_df["Correlation"] = pd.Series(logreg.coef_[0])
coeff_df.sort_values(by='Correlation', ascending=False)



# Support Vector Machines

svc = SVC()
svc.fit(X_train, Y_train)
acc_svc = round(svc.score(X_train, Y_train) * 100, 2)
print acc_svc


#KNN

knn = KNeighborsClassifier(n_neighbors = 5) #n-neighbors should be deciede by cross validation
knn.fit(X_train, Y_train)
acc_knn = round(knn.score(X_train, Y_train) * 100, 2)
print acc_knn


##Gaussian Naive bayes

gaussian = GaussianNB()
gaussian.fit(X_train, Y_train)
acc_gaussian = round(gaussian.score(X_train, Y_train) * 100, 2)
print acc_gaussian


##Random Forest
random_forest = RandomForestClassifier(n_estimators=100)
random_forest.fit(X_train, Y_train)
random_forest.score(X_train, Y_train)
acc_random_forest = round(random_forest.score(X_train, Y_train) * 100, 2)
print acc_random_forest













