import streamlit as onxy

onxy.title("Welcome to my page")

button = onxy.button("Hahahahaha")
button2 = onxy.button("Hihihihihi")
button3 = onxy.button("hehehehehe")

if button:
    onxy.balloons()

if button2:
    onxy.snow()
    
if button3:
    onxy.balloons()
    onxy.snow()
    onxy.write("pst its a secret don't tell")