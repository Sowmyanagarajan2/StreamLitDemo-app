# pip install scikit-learn
import streamlit as st
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

#train the model
iris = load_iris()
model = RandomForestClassifier().fit(iris.data,iris.target)
st.write("Iris Predictor")

a = st.number_input("Sepal Length")
b = st.number_input("Sepal width")
c = st.number_input("petal Length")
d = st.number_input("Petal Widhth")

if st.button("Predict"):
   pred = model.predict([[a,b,c,d]])
   st.write("Species:",iris.target_names[pred][0])
  
