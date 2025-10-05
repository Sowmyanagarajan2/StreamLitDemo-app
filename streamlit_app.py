!pip install scikit-learn
import streamlit as st
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

#train the model
iris = load_iris()
model = RandomForesTClassifier().fit(iris.data,iris.target)
st.write("Iris Predictor")
