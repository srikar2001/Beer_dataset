import altair as alt
import pandas as pd
import seaborn as sns
import streamlit as st



penguins_df = pd.read_excel("beer.xlsx")
st.dataframe(penguins_df)