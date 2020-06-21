#!/usr/bin/env python
# coding: utf-8

# In[11]:


import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier


# In[12]:


st.write("""
#Simple Iris Flower Prediction App
This app predicts the **Iris Flower** type!
""")

st.sidebar.header('User Input Parameters')


# In[21]:


def user_input_features():
    sepal_length = st.sidebar.slider('Sepal length', 4.3, 7.9, 5.4)
    sepal_width = st.sidebar.slider('Sepal width', 2.0, 4.4, 3.4)
    petal_length = st.sidebar.slider('Petal length', 1.0, 6.9, 1.3)
    petal_width = st.sidebar.slider('Petal width', 0.1, 2.5, 0.2)
    data = {'sepal_length': sepal_length,
            'sepal_width': sepal_width,
            'petal_length': petal_length,
            'petal_width': petal_width}
    features = pd.DataFrame(data, index=[0])
    return features


# In[22]:


df = user_input_features()
df.head()


# In[15]:


st.subheader('User input Parameters')
st.write(df)


# In[16]:


iris = datasets.load_iris()
X = iris.data
Y = iris.target


# In[17]:


clf = RandomForestClassifier()


# In[18]:


clf.fit(X, Y)
prediction = clf.predict(df)
prediction_proba = clf.predict_proba(df)


# In[19]:


st.subheader('Class labels and their corresponding index number')
st.write(iris.target_names)


# In[20]:


st.subheader('Prediction Probablity')
st.write(prediction_proba)


# In[ ]:



