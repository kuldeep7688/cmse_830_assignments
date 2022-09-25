import seaborn as sns
import streamlit as lt
import plotly.express as px
import plotly.express as px


df_iris = sns.load_dataset('iris')
print(df_iris.shape)
df_iris.head()

fig = px.scatter_3d(df_iris, x='sepal_length', y='sepal_width', z='petal_width',
              color='species')


lt.write("""
# Iris Dataset
How are Sepal length and Sepal width correlated in Iris Data among different species?
""")

lt.plotly_chart(fig, use_container_width=True)