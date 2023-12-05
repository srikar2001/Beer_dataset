import altair as alt
import pandas as pd

import streamlit as st



penguins_df = pd.read_csv("cleaned_beer.csv")
st.dataframe(penguins_df)
#installed a package
#added dataset