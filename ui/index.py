import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image

st.set_page_config(page_title="Cricket Team Generator",page_icon=":tada:",layout="wide")


# -- Header Section ---

with st.container():
    st.title("Cricket team with Generative AI Intelligence!")
    st.header("Generate a cricket fantasy team")
    st.subheader("This is a sample demo to enable you to generate a cricket fantasy team of 11 players")
    # st.write("Unleash the Power of Cloud Data Analytics with Our Expert Solutions")
    first_column, second_column, third_column, fourth_column, number_players = st.columns(5)
    with first_column:    
        option_1 = st.selectbox(
        'Team 1',('India', 'Australia', 'Pakistan', 'SriLanka', 'New Zealand', 'South Africa' ,'Bangaldesh', 'Afghanistan', 'Netherlands', 'England'))
    with second_column:    
        option_2 = st.selectbox(
        'Team 2',('India', 'Australia', 'Pakistan', 'SriLanka', 'New Zealand', 'South Africa' ,'Bangaldesh', 'Afghanistan', 'Netherlands', 'England'))
        # st.write('You selected:', option)
    with third_column:    
        option_3 = st.selectbox(
        'Format',('ODI', 'Test', 'T20'))
        # st.write('You selected:', option)
    with fourth_column:    
        option_4 = st.selectbox(
        'Team',('Male', 'Female'))
        # st.write('You selected:', option)
    with number_players:    
        number_players = st.number_input(
            "Number of players",min_value = 1, max_value = 11, value=5, step=1
        )    

with st.container():
    weather_forecast = st.text_area("Weather Forecast",value="Just 2 days on from the last game and the bandwagon has moved, set-up and gotten ready to get cracking again more than 1200km southwards of Visakhapatnam. Doubts were cast over the weather and if it'll allow for any play if not a full game but it seems to have cleared up in Thiruvananthapuram and the forecasts look great. ")    

with st.container():
    pitch_report = st.text_area("Pitch Report",value="It's a great wicket, doesn't have a lot of grass. The grass that's there is in patches so there could be inconsistent bounce. There could be some pace and turn. There's heavy dew expected around 7:30pm. The call would be to chase on this wicket.")    

with st.container():
    result = st.button("Generate the Team")
    if result:
        response = "We called the Gen AI API and the response is below for 11 players"
        st.text_area("Generated Team",value = response)
