# -*- coding: utf-8 -*-
"""bank.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Ry84I6KdX2uSUlRTqVCKmYdOxh3k1BdE
"""

import pandas as pd
import numpy as np

bank=pd.read_csv("Bank_Personal_Loan_Modelling.csv")

bank.head()

bank.columns

bank.dtypes

bank.isna().sum()

bank.info

bank.nunique()

cat_attr=(["Education","Securities Account","CD Account","Online","CreditCard"])
bank[cat_attr]=bank[cat_attr].astype('category')

bank.dtypes

bank.drop(["ID","ZIP Code"],axis=1,inplace=True)

bank.Personal_Loan.value_counts()

from sklearn.model_selection import train_test_split

y=bank["Personal_Loan"]
X=bank.drop('Personal_Loan',axis=1)

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.20,random_state=123)

print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)

num_attr=X_train.select_dtypes(['int64','float64']).columns
num_attr

from sklearn.preprocessing import StandardScaler

scaler=StandardScaler()

X_train[num_attr]=scaler.fit_transform(X_train[num_attr])

X_test[num_attr]=scaler.transform(X_test[num_attr])

print(X_train.shape)
print(X_test.shape)

from sklearn.linear_model import LogisticRegression

lr=LogisticRegression()

lr.fit(X_train,y_train)

X_train_pred=lr.predict(X_train)
X_test_pred=lr.predict(X_test)

from sklearn.metrics import accuracy_score,precision_score,recall_score

accuracy_score(y_train,X_train_pred)

accuracy_score(y_test,X_test_pred)

import pickle

pickle.dump(lr, open('model.pkl','wb'))

model = pickle.load(open('model.pkl','rb'))

