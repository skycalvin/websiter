import streamlit as st
st.set_page_config(layout='wide')

st.title('Toy Conversion App')

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
                'milk':319/42.3,
                'instant noodles':319/340},
    'weight': {"gr":1/0.001,
                "kg":1,
                "ton":1/1000,
                "adult person":1/75,
                "a teenager":1/60,
                "cat":1/3.5,
                "mouse":1/0.450,
                "dog":1/1.4,
                "cow":1/1800,
                "elephant":1/4000,
                "giraffe":1/1200,
                "penguin":1/23,
                "dolphin":1/4000,
                "blue whale":1/150000,
                "brontosaurus":1/22000,
                "t-rex":1/8000},
    'toys' : {"NERF":800000/800000,
                "lego":800000/320000,
                "hotwheels":800000/27500,
                "monster jam":800000/155000,
                "transformers":800000/490000,
                "godzilla":800000/219000,
                "ghidorah":800000/482000,
                "lamborghini":800000/59000,
                "jaeger":800000/260000,
                "Mario":800000/299000,
                "gundam HG":800000/600000,
                "gundam MGEX":800000/2000000,
                "gundam PG":800000/4000000,
                "gundam RG":800000/650000,
                "gundam SD":800000/185000,
                "gundam MGSD":800000/220000,
                "gundam MG":800000/930000,
                "gundam MG 2.0":800000/1000000,
                "kong":800000/512000},
    'time': {'seconds':3600,
                'minutes':60,
                'hour':1,
                'day':1/24,
                'week':1/((24*7)),
                'month':1/(24*30),
                'year':1/(24*365),
                'cat year':1/(24*365*5),
                'dog year':1/(24*365*5)}}
picture_link = {"NERF":'./images/nerf_gun.jpg',
                "lego":'./images/lego.jpg',
                "hotwheels":'./images/hotwheels.jpg',
                "monster jam":'./images/monster_jam.jpg',
                "transformers":'./images/transformers.jpg',
                "godzilla":'./images/godzilla.jpg',
                "ghidorah":'./images/ghidorah.jpg',
                "lamborghini":'./images/lamborghini.jpg',
                "jaeger":'./images/jaeger.jpg',
                "Mario":'./images/mario.jpg',
                "gundam HG":'./images/gundam_HG.jpeg',
                "gundam MGEX":'./images/gundam_MGEX.jpg',
                "gundam PG":'./images/gundam_PG.jpg',
                "gundam RG":'./images/gundam_RG.jpg',
                "gundam SD":'./images/gundam_SD.jpg',
                "gundam MGSD":'./images/gundam_MGSD.jpg',
                "gundam MG":'./images/gundam_MG.jpg',
                "gundam MG 2.0":'./images/gundam_mg2.0.jpg',
                "kong":'./images/kong.jpg'}

col1,col2,col3,col4,col5 = st.columns(5)

#category selection
with col1:
    category_list = list(conversion_factors.keys())
    category = st.radio("Select category",options=category_list,index=3)

with col2:
   input_value = st.number_input("Input",min_value=1,value=1)


with col3:
  base_unit_list = list(conversion_factors[category].keys())
  base_unit = st.radio("From:",options=base_unit_list)
  base_cf = conversion_factors[category][base_unit]
  st.image(picture_link[base_unit])

with col4:
  target_unit_list = list(conversion_factors[category].keys())
  target_unit = st.radio("To:",options=target_unit_list)
  target_cf = conversion_factors[category][target_unit]
  st.image(picture_link[target_unit])

with col5:
  st.write("output")
  output_value = input_value / base_cf * target_cf
  st.write(f'The {category} of {input_value} {base_unit} equals to {output_value:.2f} {target_unit}')

