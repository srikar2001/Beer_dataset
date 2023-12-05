import altair as alt
import pandas as pd

import streamlit as st



penguins_df = pd.read_excel("cleaned_beer.xlsx")
st.dataframe(penguins_df)
#installed a package