# Jupyter Notebook: Analyzing Titanic Dataset

## 1. Import Libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

## 2. Load Data
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
data = pd.read_csv(url)
# print("Dataset Shape:", data.shape)
# print(data.columns)
data['Age'] = data['Age'].fillna(data['Age'].median())
data['Embarked']=data['Embarked'].fillna(data['Embarked'].mode()[0])
# print(data.describe())
# print(data.isnull().sum())
# print(data.head())

survival_rate = data.groupby('Pclass')['Survived'].mean()
# print(survival_rate)

