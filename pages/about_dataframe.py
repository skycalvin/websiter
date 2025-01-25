65import pandas as pd
import streamlit as st

data = pd.read_excel('./pages/source.xlsx')
unique_category = data['category'].unique()
unique_store_name = data['store_name'].unique()

selected_category = st.multiselect("select category",options=unique_category)
selected_store_name = st.multiselect("select store_name",options=unique_store_name)

criteria1 = data['category'].isin(selected_category)

criteria2 = data['store_name'].isin(selected_store_name)
criteria3 = data['price'] > 12000
criteria4 = (data['price'] >= 12000) & (data['price'] <= 40000)
criteria5 = (criteria1) & (criteria2) & (criteria3)

data = data[criteria1]

#print(data[criteria5])
print(data[criteria5].sort_values('price',ascending=True))
st.dataframe(data)
