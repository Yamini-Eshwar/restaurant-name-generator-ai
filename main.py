import streamlit as st
import langchain_helper
import re

st.title('Restaurant Name Generator')


st.markdown(
    """
    <style>
    /* Sidebar container */
    section[data-testid="stSidebar"] {
        background-color: white !important;
        color: black !important;
        padding: 1rem;
        border-right: 2px solid #eee;
    }

    /* Sidebar image centering */
    section[data-testid="stSidebar"] img {
        display: block;
        margin: 0 auto 20px;
        border-radius: 10px;
        box-shadow: 0 0 8px #ddd;
    }

    /* Glowing red border for dropdown */
    section[data-testid="stSidebar"] .stSelectbox > div {
        border: 2px solid red !important;
        box-shadow: 0 0 10px red !important;
        border-radius: 6px !important;
    }

    /* Main page background image */
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1414235077428-338989a2e8c0?q=80&w=1170&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        color: white !important;
    }

    /* Content box styling */
    .block-container {
        background-color: rgba(0, 0, 0, 0.6); /* semi-transparent black */
        padding: 2rem;
        border-radius: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)


st.sidebar.image("https://miro.medium.com/v2/resize:fit:1358/1*z9LK7Yuahbb5U64rEbIDqg.jpeg", use_column_width=True)


cuisine = st.sidebar.selectbox("Pick a Cuisine", ("Indian", "Italian", "Mexican", "American", "Arabic"))

print(cuisine)

if cuisine:
    response = langchain_helper.get_restaurant_name_and_items(cuisine)
    restaurant_name = re.sub(r'^"|"$', '', response['restaurant_name'].strip())
    st.header(restaurant_name)
    menu_items = response['menu_items'].strip().split(',')

    st.write("**Menu Items**")
    for item in menu_items:
        st.write(item)

    