
# TODO regional response.


import requests
import json
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image
import requests

api_url = "http://x.x.x.x:5000/genai"
# prompt = {"prompt":"Generate a fantasy cricket team for the upcoming odi match between India vs Australia for male players. My budget is 100 credits, and I need to select 11 players, including criteria for player selection, e.g., a minimum number of batsmen, bowlers, all-rounders, and wicket-keepers."}

st.set_page_config(page_title="Cricket Team Generator",page_icon=":tada:",layout="wide")


# -- Header Section ---

with st.container():
    st.title("Cricket team with Generative AI Intelligence!")
    st.header("Generate a cricket fantasy team")
    st.subheader("This is a sample demo to enable you to generate a cricket fantasy team of 11 players")
    # st.write("Unleash the Power of Cloud Data Analytics with Our Expert Solutions")
    first_column, second_column, third_column, fourth_column, series, venue = st.columns(6)
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
    with series:    
        series_current = st.selectbox(
        'Series',('India vs Australia T20', 'New Zealand Tour of Bangaldesh'))
    with venue:    
        venue_selection = st.selectbox(
        'Venue',('Wankhede', 'Visakhapatnam', 'Guhwati', 'Pune'))
    if option_1 == option_2:
        st.error('Please select two different teams')     

with st.container():
    weather_forecast = st.text_area("Weather Forecast",value="Just 2 days on from the last game and the bandwagon has moved, set-up and gotten ready to get cracking again more than 1200km southwards of Visakhapatnam. Doubts were cast over the weather and if it'll allow for any play if not a full game but it seems to have cleared up in Thiruvananthapuram and the forecasts look great. ")
    if weather_forecast == "":
        st.error('Weather Forecast cannot be empty')          
with st.container():
    pitch_report = st.text_area("Pitch Report",value="It's a great wicket, doesn't have a lot of grass. The grass that's there is in patches so there could be inconsistent bounce. There could be some pace and turn. There's heavy dew expected around 7:30pm. The call would be to chase on this wicket.")    
    if pitch_report == "":
        st.error('Pitch Report cannot be empty')  
with st.container():
    result = st.button("Generate the Team")
    if result:
        base_prompt = "Generate a fantasy cricket team for the upcoming " + option_3 +" match between " + option_1 + " vs " + option_2 + " for male players. My budget is 100 credits, and I need to select 11 players, including criteria for player selection, e.g., a minimum number of batsmen, bowlers, all-rounders, and wicket-keepers."
        prompt = base_prompt
        prompt = prompt + ". Weather Report :  " + weather_forecast
        prompt = prompt + ". Pitch Report :  " + pitch_report
        prompt = prompt + "Consider the pitch report and weather report before selecting the team. In the reasons for selecting players, mention if you took pitch/weather conditions in consideration while selecting that particular player."
        prompt = prompt + "Higher the risk appetite, the more you are allowed to choose upcoming players that are predicted perform well in this match. Lower the risk taking nature, stick with players who have proved to perform well in history.Now form the team according to a moderate risk appetite."
        prompt = prompt + "Give the team in the following format:"
        prompt = prompt + "Player1: Reason for taking Player1. Player2: Reason for taking Player2. Player3: Reason for taking Player3 Player4: Reason for taking Player4 and so on"
        prompt = prompt + "Captain: Player Name and reason and Vice Captain: Player Name and reason"
        prompt = prompt + "Reason for overall team strength and why it would perform well"

        final_prompt = json.loads('{"prompt":"' + prompt + '"}')
        response = requests.post(api_url, json=final_prompt)
        # print(response.text)
        st.text_area("Generated Prompt",value = final_prompt, height = 200)
        st.text_area("Generated Team",value = response.text, height = 500)
