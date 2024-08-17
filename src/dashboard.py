import streamlit as st
from src.main import generate_memorable_password, generate_random_password, generate_pin

st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRArw1dvFe9GhlKbDsws46nr8a-BzPo85eUJg&s")
st.title(":lock: Password Generator")

option = st.selectbox("What kind of password do you need?",
("Pin Code", "Random", "Memorable"),
index=None)


if option == "Pin Code":
    length = st.slider("please choose the desired length. ",
    4, 12)
    st.write("Your password is: \n", generate_pin(length=length))
elif option == "Random":
    length = st.slider("please choose the desired length. ", 4, 12)
    st.write("What do you want to be included in the password?")
    include_num = st.toggle("Number")
    include_sym = st.toggle("Symbol")
    st.write("Your password is: \n", generate_random_password(length=length,
    include_num=include_num,
    include_sym=include_sym))
else:
    num_words = st.slider("please choose the number of words. ",
    2, 6)
    sep = st.text_input("Enter the seperator?")
    capitalization = st.toggle("capitalization")
    st.write("Your password is: \n", generate_memorable_password(num_of_words=num_words,
    separator=sep,
    capitalize=capitalization))
