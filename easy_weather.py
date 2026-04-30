import streamlit as st
import requests

st.title(":blue[EASY] :yellow[WEATHER]")

c1,c2,c3=st.columns(3)

with c1:
    st.image("https://th.bing.com/th/id/OIP.9gTyRnlS2-oWwXM0vnc5ngHaE6?w=261&h=180&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3",width=300)
with c2:
    st.image("https://th.bing.com/th/id/OIP.3nGwh90_uecuOh08tuwGsgHaEo?w=260&h=180&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3",width=300)
with c3:
    st.image("https://th.bing.com/th/id/OIP.9hVOQwz5HOaQ9ctPBqUKmQHaEo?w=301&h=188&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3",width=300)
city = st.text_input("Enter city name")
unit=st.radio("Choose unit ",["celsius","faherhnite"])
api_key = "800382a46405dac27f3ee2dc779b057f"

def get_latnlon(city_name):
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=5&appid={api_key}"
    response = requests.get(url)
    return response.json()

def get_weather(lat, lon):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"
    response = requests.get(url)
    return response.json() 

if city: 
    location_data = get_latnlon(city)
    
    if location_data and len(location_data) > 0:
        lat = location_data[0]["lat"]
        lon = location_data[0]["lon"]
        
        weather_data = get_weather(lat, lon)
        
        if "main" in weather_data:
            if unit=="celsius":
                temp = weather_data["main"]["temp"] - 273.15
                st.success(f"Current Temperature in {city.title()} is {int(temp)} °C")
            elif unit=="faherhnite":
                temp= (weather_data["main"]["temp"]-273.15)*(9/5) + 32
                st.success(f"Current Temperature in {city.title()} is {int(temp)} °F") 
        else:
            st.error("Error fetching temperature data from OpenWeather.")
            
        if "weather" in weather_data:
            if unit:
                weather=weather_data["weather"][0]["description"]
                st.success(f'{weather.title()}')
        else:
            st.error("Error fetching weather data from OpenWeather.")    
                
        if "wind" in weather_data:
            if unit:
                speed=weather_data["wind"]["speed"]
                st.success(f'Wind speed is {speed}km/hr')
        else:
            st.error("Error fetching wind speed data from OpenWeather.")    
                        
    else:
        st.error(f"Could not find coordinates for '{city}'")
   