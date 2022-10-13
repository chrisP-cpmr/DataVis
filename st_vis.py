import pandas as pd
import streamlit as st
import altair as alt

df = pd.read_csv("Data_clean_v2.csv")

df = df.rename(columns={"country":"Country", "commodity":"Commodity", "year":"Year", "loss_percentage":"Loss Percentage", "food_supply_stage":"Supply Chain Stage"})

# st.altair_chart
c = alt.Chart(df).mark_circle().encode(
     x='Supply Chain Stage', y='Year', size='Loss Percentage', color='Loss Percentage', tooltip=['Supply Chain Stage', 'Year', 'Loss Percentage'])

st.altair_chart(c, use_container_width=True)


# add df with only 3 columns
df_simple = df[['Supply Chain Stage', 'Year', 'Loss Percentage']]


#st.line_chart
chart_data = df_simple

st.line_chart(chart_data)




