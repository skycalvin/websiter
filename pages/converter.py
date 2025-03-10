import streamlit as st

st.title('Fun Conversion App')

conversion_factors = {
            'distance': {'mm':1,
                        'cm':1/0.1,
                        'm':1/0.01},
            'calories': {'fries':319/319,
                        'donut':319/190,
                        'burger':319/290,
                        'ice cream':319/207,
                        'apple':319/52.1,
                        'banana':319/88.7,
                        'cabbage':319/24.6,
                        'coke':319/139,
                        'milk':319/42.3},
                        'instant noodles':319/340},
           # "weight": {"gr":1/0.001,
                        #"kg":1,
                        #"ton":1/1000,
                        #"adult person":1/75,
                        #"a teenager":1/60,
                        #"cat":1/3.5,
                        #"mouse":1/0.450,
                        #"dog":1/1.4,
                        #"cow":1/1800,-
                        #"elephant":1/4000,
                        #"giraffe":1/1200,
                        #"penguin":1/23,
                        #"dolphin":1/4000,
                        #"blue whale":1/150000,
                        #"brontosaurus":1/22000,
                        #"t-rex":1/8000},
            'toys' : {"NERF":800000/800000,
                        "lego":320000/800000,
                        "hotwheels":27500/800000,
                        "monster jam":155000/800000,
                        "transformers":490000/800000,
                        "godzilla":219000/800000',
                        "ghidorah":482000/800000,
                        "lamborghini":59000/800000,
                        "jaeger":260000/800000,
                        "Mario":299000/800000,
                        "gundam HG":600000/800000,
                        "gundam MGEX":2000000/800000,
                        "gundam PG":4000000/800000,
                        "gundam RG":650000/800000,
                        "gundam SD":185000/800000,
                        "gundam MGSD"220000/800000,
                        "gundam MG":930000/800000,
                        "gundam MG 2.0":1000000/800000,
                        "kong":512000/800000},
            'time': {'seconds':3600,
                        'minutes':60,
                        'hour':1,
                        'day':1/24,
                        'week':1/((24*7)),
                        'month':1/(24*30),
                        'year':1/(24*365),
                        'cat year':1/(24*365*5),
                        'dog year':1/(24*365*5)}

col1,col2.col3,col4,col5 = st.columns(5)

#category selection
with col1:
category_list = list(conversion_factors.keys())
category = st.radio("Select category",options=category_list)

with col2:
  st.write("Input")


with col3:
  base_unit_list = list(conversion_factors[category].keys())
  base_unit = st.radio("From:",options=base_unit_list)

with col4:
  target_unit_list = list(conversion_factors[category].keys())
  target_unit = st.radio("To:",options=target_unit_list)

with col5:
  st.write("output")
